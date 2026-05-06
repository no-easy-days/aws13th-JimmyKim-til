# ArgoCD GitOps 연동 과정
- Toy-Project에서 진행한, EKS에 배포된 어플리케이션을 ArgoCD로 `GitOps` 방식으로 관리하기 위한 과정


## 전체 흐름

```
GitHub Repo (yaml 파일)
      ↓ (sync)
ArgoCD (EKS A - Hub)
      ↓ (deploy)
EKS A / EKS B / EKS C
```

---

## 1. Git Repo 구조 정리 (선행 작업)

ArgoCD는 Git Repository를 바라보고 sync하는 구조라, 당연히 `yaml` 파일들이 Git에 올라가 있어야 한다.

권장 디렉토리 구조:
```
gitops-repo/
└── manifests/
    └── board-app/
        ├── base/                   # 공통 리소스
        │   ├── Namespace.yaml
        │   ├── Deployment.yaml
        │   ├── Service.yaml
        │   ├── Ingress.yaml
        │   ├── Configmap.yaml
        │   ├── SecretProviderClass.yaml
        │   └── kustomization.yaml
        └── overlays/
            ├── prod/               # EKS A
            │   └── kustomization.yaml
            ├── staging/            # EKS B
            │   └── kustomization.yaml
            └── dr/                 # EKS C
                └── kustomization.yaml
```

base/kustomization.yaml:
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - Namespace.yaml
  - Deployment.yaml
  - Service.yaml
  - Ingress.yaml
  - Configmap.yaml
  - SecretProviderClass.yaml
```

overlays/prod/kustomization.yaml:
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
bases:
  - ../../base
patches:
  - patch: |-
      - op: replace
        path: /spec/replicas
        value: 2
    target:
      kind: Deployment
      name: board-app
```

---

## 2. ArgoCD 설치 (EKS A - Hub 클러스터)

```bash
# ArgoCD 네임스페이스 생성 및 설치
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# 설치 확인
kubectl get pods -n argocd -w
```

ArgoCD UI 접근 (LoadBalancer로 노출):
```bash
kubectl patch svc argocd-server -n argocd \
  -p '{"spec": {"type": "LoadBalancer"}}'

# 초기 admin 패스워드 확인
kubectl get secret argocd-initial-admin-secret -n argocd \
  -o jsonpath='{.data.password}' | base64 -d

# URL 확인
kubectl get svc argocd-server -n argocd
```

ArgoCD CLI 설치:
```bash
curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
chmod +x argocd && mv argocd /usr/local/bin/

# CLI 로그인
argocd login <ARGOCD_SERVER_URL> --username admin --password <패스워드> --insecure
```

ArgoCD ~ GitHub 연동(Private):
```bash
argocd repo add https://github.com/kjhappy77/aws13th-K8s-Project.git \
  --username kjhappy77 \
  --password <GitHub Personal Access Token>

# GitHub PAT 없으면 GitHub → Settings → Developer settings → Personal access tokens → Generate new token에서 repo 권한으로 발급
```
---

## 3. Spoke 클러스터 등록 (Hub-Spoke 구성 시)

- EKS B, EKS C를 ArgoCD에 등록해야 한다. 그 전에, 내 로컬 환경에서 `kubeconfig`에 해당 클러스터에 대한 context가 있어야 한다.
- 클러스터 구성 완료 후, `aws eks update-kubeconfig`로 `kubeconfig`파일 export 후, argoCD에 merge하여 `argocd cluster add` 실행 필요.

```bash
# 현재 등록된 클러스터 확인
argocd cluster list

# EKS B 등록
argocd cluster add <EKS-B-CONTEXT-NAME> --name eks-b-staging

# EKS C 등록
argocd cluster add <EKS-C-CONTEXT-NAME> --name eks-c-dr
```

context 이름 확인:
```bash
kubectl config get-contexts
```

---

## 4. ArgoCD Application 생성

### 방법 1 - CLI로 생성

```bash
argocd app create board-app-prod \
  --repo https://github.com/<계정>/<gitops-repo> \
  --path apps/board-app/overlays/prod \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace board-app-eks \
  --sync-policy automated \
  --auto-prune \
  --self-heal
```

- 이 방법도 있긴하지만, 기록이 남지 않다보니... 언제나 `yaml` 파일을 통해 진행하는 것이 안전하다.


### 방법 2 - yaml로 생성 (권장)

```yaml
# argocd-app-prod.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: board-app-prod
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/<계정>/<gitops-repo>
    targetRevision: main
    path: manifests/board-app/overlays/prod
  destination:
    server: https://kubernetes.default.svc   # EKS A (로컬)
    namespace: board-app-eks
  syncPolicy:
    automated:
      prune: true       # Git에서 삭제된 리소스 자동 제거
      selfHeal: true    # 수동 변경 감지 시 자동 복구
    syncOptions:
      - CreateNamespace=true
```

```bash
kubectl apply -f argocd-app-prod.yaml
```

EKS B (staging) Application:
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: board-app-staging
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/<계정>/<gitops-repo>
    targetRevision: main
    path: manifests/board-app/overlays/staging
  destination:
    server: <EKS-B-SERVER-URL>   # argocd cluster list에서 확인
    namespace: board-app-eks
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

---

## 5. App of Apps 패턴 (여러 클러스터 한 번에 관리 목적)

***“ArgoCD로 ArgoCD를 관리한다.”***
여러 개의 Application 리소스를 하나의 상위 Application으로 묶어서 GitOps 방식으로 관리함. <br>
EKS 클러스터 3개를 연동해야하는 상황이었기 때문에, argoCD가 구동되는 주요 클러스터에 가장 상위 argoCD App을 생성하고, <br>
실제 운영환경용 클러스터에 배포할 App 리스트를 명시한 yaml 파일 / 나머지 2개의 클러스터에 배포할 App 리스트를 명시할 yaml 파일을 작성했다.

```yaml
# argocd-app-of-apps.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: app-of-apps
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/<계정>/<gitops-repo>
    targetRevision: main
    path: argocd-apps/
  destination:
    server: https://kubernetes.default.svc
    namespace: argocd
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

---

## 6. 배포 확인

```bash
# Application 상태 확인
argocd app list

# 상세 상태
argocd app get board-app-prod

# 수동 sync
argocd app sync board-app-prod

# sync 히스토리
argocd app history board-app-prod
```

UI에서도 동일하게 확인 가능하다. `http://<ARGOCD_SERVER_URL>`

---

## 7. GitOps 배포 흐름 (이후 운영)

```
코드/yaml 수정
    ↓
git push → GitHub
    ↓
ArgoCD가 변경 감지 (기본 3분 폴링, 또는 Webhook 설정)
    ↓
자동 sync → EKS에 반영
```

Webhook 설정하면 push 즉시 반영 :
- GitHub Repo → Settings → Webhooks
- Payload URL: `https://<ARGOCD_SERVER_URL>/api/webhook`
- Content type: `application/json`

---

## 주의사항

- `Secret.yaml`은 Git에 올리면 안 된다. Secrets Manager + SecretProviderClass 방식으로 대체하거나, Sealed Secrets 사용 권장
- `db_init_Job.yaml`은 최초 1회만 실행하면 되므로 ArgoCD sync 대상에서 제외하거나 `argocd.argoproj.io/hook: PreSync` 어노테이션 활용

# AWS 자체적으로 만들어둔 모듈도 있고, 개발자가 만들어둔 모듈도 있다 --> DockerHub, ECR 같은 일종의 "레지스트리"가 있다!
# 레지스트리 주소 : https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest
# 기본적인 모듈 선언 방법은 레지스트리 웹 페이지에서 확인하여 사용하면 된다. 
# 세부 설정 값들은 문서 확인해서 코드 작성하자. 업데이트 되어서 변경되는 경우도 있다.

module "eks" {
    source = "terraform-aws-modules/eks/aws"
    version = "~> 20.0"
    # 기본 모듈 불러오기, 최신 버전이 문제가 있어서... 일단 20 버전으로 했음
    name = "pub-cluster"
    # 클러스터 이름
    kubernetes_version = "1.35"
    endpoint_public_access = true
    # 외부에서 kubectl 명령어를 사용할 수 있도록 허용
    enable_cluster_creator_admin_permissions = true
    # Optional: Adds the current caller identity as an administrator via cluster access entry
    vpc_id = var.eks-vpc-id
    subnet_ids = [
        var.pub-sub1-id,
        var.pub-sub2-id
    ]
    # 여러개 불러올때는 List 형태로 대괄호로 입력한다.
    # vpc_id, subnet_id는 다른 디렉토리에서 선언해뒀다.(outputs.tf는 이미 구성되어있음)
    # 이를 참조해서 가져오기 위해 variables.tf가 필요하며, variables.tf에 잘 명시해뒀으면 var 활용하면 된다.
    eks_managed_node_groups = {
        eks_nodegroup = {
            min_size = 2
            max_size = 5
            desired_size = 2
            instance_types = ["t3.micro"]
            # 리스트 형태로 넣어줌(테라폼 문법)
        }
    }
    # NodeGroup 선언
}




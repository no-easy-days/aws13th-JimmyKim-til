## 2번째 딥다이브 - 인증과 토큰 (Authentication & Token)

### ❓ 힌트
- **Stateless(무상태성) / Cookie(쿠키) / Session(세션)**
- **JWT(Json Web Token) / Authorization Header**

1. HTTP는 Stateless 성질을 가진다. 서버는 어떻게 기억할까?
    - Session을 쓰면 기억한다고 볼수 있고, Cookie와 Token으로는 기억은 못하지만 통행증 확인 정도만 한다. 
2. Session vs Token/JWT 장,단점
    - Session은 서버에 저장되는 것, Token/JWT는 클라이언트에 저장되는 것. 저장 리스크를 생각하면 된다.
3. JWT는 아주 긴 문자열 형태. Decode 했을 때 사용자 ID가 들어가있을까?
    - 토큰은 USER ID로 주인을 "식별"한다. 이것은 식별자 "Identifier" 이고, 결국 포함되는 걸 권장한다.
    - 들어가있으면 안되는건 민감하고 소중한 정보들이다.

---

## 필요 개념 정리

### 1. Stateless
- 서버는 단순히 응답만을 수행한다.
- **모든 정보는 클라이언트가 가지고 있다**가, 서버 통신 시 데이터를 실어 보낸다.
- Stateful에 비해 더 많은 데이터가 소모된다.

### 2. Cookie
- **클라이언트의 브라우저에 설치되는 기록 정보 파일.**
> Key & Value 쌍 문자열의 덩어리로 이루어져있다.

1. 클라이언트 → 서버 최초 접속 시, 서버에서 쿠키 허용 요청
2. 허용 시, 서버 → 클라이언트로 Response Header ~ `Set-Cookie`에 담음
3. 클라이언트 → 서버 두번째 접속부터 Request Header ~ `Cookie`에 담아 보냄

- **단점**
    - 브라우저간 차이 존재
    - 용량 제한이 존재
    - 보안 취약 (Request할때 쿠키 그대로 담기 때문에)

### 3. Session
- Cookie의 보안 취약성으로, **민감한 Authentication 정보를 서버 측에서 저장 & 관리**
- **Cookie와 함께 사용**된다. (서버로 Request할 때, Session ID를 Cookie에 담아서 전송)
> Key(Session ID) & Value(다양한 속성들) 쌍 문자열의 덩어리로 이루어져있다. (Cookie와 형태는 동일)

- **단점**
    - 세션 ID 자체를 탈취당하면 다른 클라이언트가 위장을할 수 있기 때문에 위험해진다.
    - 결국엔 서버에 저장하는 것이기 때문에 클라이언트 늘어나면 부하 증가



### 4. Token
- Stateless를 유지하며 동시에 Authorization 상태를 유지하기 위한 기술
- 토큰은 **클라이언트에 저장**, 서버의 부담을 줄일 수 있음.

1. 클라이언트 → 서버 최초 접속 시, Authentication 완료되었다는 의미로 서버에서 토큰 발급
2. 이후 클라이언트 → 서버 Request 시 토큰 정보를 계속 확인해서 일치 여부 체크

- **단점**
    - 네트워크 부하, 탈취 당하면 끝장남, 중요 정보 담을 수 없음(Payload는 암호화 X)

### 5. JWT Token (JSON Web Token)
- Authentication을 암호화 시킨 JSON 형태의 토큰. 여기서 "JWT 기반 인증" 이라는 말이 나옴.
- JSON 데이터를 **Base64 URL-safe Encode 를 통해 인코딩 & Serialization** 한 것
- `.`을 구분자로 사용하고, **Header(헤더), Payload(본문), Signature(전자서명)** 부분로 구성

#### 1) 구성 요소
- **A) Header** : type 정보와 Hash 알고리즘 종류
- **B) Payload** : 서버에서 필요한 사용자 Authentication & Authorization 및 기타 정보
    - `Registed claims` : iss(발행자), exp(만료시간), sub(제목), iat(발행시간), jti(JWT ID)
    - `Public claims` : 공개용 정보
    - `Private claims` : 당사자들 간 정보 공유를 위해 만들어진 정보
- **C) Signature** : 전자 서명값. 
    - Base64{Header} + Base64{Payload} 형태에서, 개인 키를 키값으로 사용하여 Hash 암호화.
    - **개인 키(Private Key)** : 서버만 알고 있는 고유 키. **토큰 위변조 검증의 핵심**, 유출되면 위험함.
    - 최종 결과 값: 해싱한 바이너리 데이터를 다시 Base64 URL-safe로 인코딩

$$
\text{Signature} = \text{Base64UrlEncode}\Big(\text{HMAC-SHA256}\big(
\text{Base64UrlEncode}(\text{Header}) + "." + \text{Base64UrlEncode}(\text{Payload}), \text{SecretKey}
\big)\Big)
$$

> 결국 전체 구성 요소는 `Base64{Header}.Base64{Payload}.[Signature]` 형태이다.

#### 2) 사용 목적은? → ***서명(Authentication), 위조 방지***
- Signature 부분의 개인 키를 모르기 때문에 인증이 가능한 것.
- **장점** : 빠름, **서버가 Stateless 상태**가 되어 확장성 우수
- **단점** : 토큰 관리 못하면 답 없음 (탈취 시 대처 어려움)

#### 3) 대표적인 사용 방식
1. 클라이언트 → 서버 로그인 요청
2. 서버 → 클라이언트 Authentication 완료. **액세스 토큰**, **리프레시 토큰** 발급 (*여기서 저 두가지 토큰이 JWT !*)
3. 클라이언트 → **서버 액세스 토큰** 사용 API 요청
    - 액세스 토큰 문제 발생(만료 등) → 리프레시 토큰으로 액세스 토큰 재발급 요청



### 6. Authorization Header
- 위에 인"증"을 위해 만들어둔 친구들을 서버에 인"가"받기 위해 보내는 부분
- 해외갈 때 출입국 심사를 생각해보면 이해하기 쉬움.

---

### 📝 추가 키워드

- **Authentication(인증) vs Authorization(인가)**
    - "민증 보여주는 것 (신원 확인)" vs "통행 허가, 길 열어주는 것 (권한 부여)"
- **Payload**
    - 실제 담기는 데이터, 본문 내용
- **Base64 URL-safe Encode**
    - URL을 암호화 할때 복호화하고 나서 URL이 망가지는걸 방지하기 위해 `+`, `/` 기호를 각각 `-`, `_` 로 치환하는 방식. 나머지는 Base64 암호화 규칙 따름
- **Base64 Encode**
    - **바이너리 데이터 → 텍스트로 변경하는 방식**의 일종. (속칭 64진법)

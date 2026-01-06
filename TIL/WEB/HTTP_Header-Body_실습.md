## 문제 1: HTTP 요청 메시지 분석

```
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer token_xyz_123
Content-Length: 67

{
    "name": "임태종",
    "email": "[taejong@example.com](mailto:taejong@example.com)"
}
```

1. 이 요청의 HTTP 메서드
   > **POST**
2. 요청 받는 서버 주소
   > api.example.com/api/users
3. Body의 데이터 형식
   > json
4. 어떤 작업인지 설명
   > 이름과 이메일 주소를 생성

## 문제 2: HTTP 응답 메시지 작성
 1) 상태코드 : 201 (Created)
 2) 응답 데이터 형식 : JSON
 3) 응답 내용 : 사용자 생성 성공 메시지와 생성된 사용자 ID (12345)

```
========== Start Line ==========
# HTTP/1.1: HTTP 버전
# 200: 상태 코드 (성공)
# OK: 상태 메시지
HTTP/1.1 201 Created

# ========== Headers ==========
# Content-Type: 응답 데이터가 JSON 형식임을 알림
Content-Type: application/json

# Content-Length: Body의 크기
Content-Length: 89

# Set-Cookie: 브라우저에 세션 쿠키를 저장하라는 지시
Set-Cookie: session=abc123xyz; HttpOnly; Secure

# Date: 응답이 생성된 시간
Date: Sun, 04 Jan 2026 11:30:00 GMT

# ========== 빈 줄 (Header와 Body 구분) ==========

# ========== Body ==========
# 서버가 전달하는 응답 데이터
{
    "status": "사용자 생성 성공",
    "userId": 12345
}
```

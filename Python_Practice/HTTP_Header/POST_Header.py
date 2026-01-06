#pip install requests
import requests
import json

# 2. POST 요청으로 데이터 전송하기
# 2-1. JSON 포맷으로 보내보자.

# 보낼 데이터 (Body)
user_data = {
    "name": "jaehyun_jimmy_kim",           # 사용자 이름
    "email": "kjhappy77@gmail.com",  # 이메일
    "role": "student"      # 역할
}

# 요청 Header 설정
# 기본적으로 MIME type에 등록된 걸 따라가자.
# 접두사 "X"는 사용자가 커스텀해서 만들어줄 때 붙여서 명시한다.
headers = {
    "Content-Type" : "application/json",
    "Authorization" : "Bearer my_token_123",
    "X-Custom-Header" : "Jaehyun Jimmy Kim"
}
print("=" * 50)
print("Request 정보:")
print("=" * 50)
print(f"  URL: https://httpbin.org/post")
print(f"  사용할 HTTP Method: POST")
# 실제 전달할 Json 형태 데이터 print로 찍어보기
print(f"    Headers: {json.dumps(headers, ensure_ascii=False, indent=2)}")
print(f"    Body: {json.dumps(user_data, ensure_ascii=False, indent=2)}")

# 실제 요청 시작
response = requests.post("https://httpbin.org/post", headers=headers, json=user_data)

# 요청했고, 이제 응답 확인
print("=" * 50)
print("Response 정보:")
print("=" * 50)
# 실제 응답 받은 데이터를 특정 변수에 할당
print(f"  상태 코드: {response.status_code}")
response_data = response.json()
print(f"  서버가 받은 Header : ")
for key, value in response_data['headers'].items():
    print(f"    {key} : {value}")
print(f"  서버가 받은 Body (Json 형태) : ")
print(f"  {response_data['json']}")

# 2-2 Form 데이터 전송
login_data = {
    "username" : "Jaehyun Jimmy Kim",
    "password" : "asdqwe123!@#"
}

# FormData 형식으로 Post 요청
# JSON 형식이 아니기 때문에, json=  안쓰고 data=  씀
response = requests.post("https://httpbin.org/post", data=login_data)
print("=" * 50)
print("FormData 전송 결과:")
print("=" * 50)

result = response.json()
print(f"Content-Type: {result['headers']['Content-Type']}")
print(f"전송된 Form 데이터: {result['form']}")
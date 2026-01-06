import requests
import json

# 3-1. 요청 Header 확인
response = requests.get("https://httpbin.org/headers",
                        headers={
                            "Accept" : "application/json",
                            "Accept-Language" : "ko-KR",
                            "X-Requested-By" : "Jaehyun Jimmy Kim"
                        }
                        )

print("=" * 50)
print("내가 보낸 Request Header:")
print("=" * 50)
# Request 보낸 객체에 접근
request = response.request
print(f"    Method: {request.method}")
print(f"    URL: {request.url}")
print(f"    Headers:")
for key, value in request.headers.items():
    print(f"    {key}: {value}")

print("=" * 50)
print("서버가 받은 실제 Request Header: <비교해보자>")
print("=" * 50)
# 서버의 Response 값 json으로 받아오기
server_received = response.json()
for key, value in server_received['headers'].items():
    print(f"    {key}: {value}")

# 3-2. 특정 Header 추출
response = requests.get("https://httpbin.org/get")

print("=" * 50)
print("Response Header 값:")
print("=" * 50)

# (1) 딕셔너리처럼 접근하기. 키값을 대괄호에 넣어주기
try:
    content_type = response.headers['Content-Type']
    print(f"    Content-Type: {content_type}")
except KeyError:
    print(f"    Content-Type이 없습니다.")

# (2) get() 메서드 활용하기 <--- 권장!!
content_length = response.headers.get('Content-Length', '알 수 없음')
print(f"    Content-Length: {content_length}")
server = response.headers.get('Server', '알 수 없음')
print(f"    Server: {server}")
date = response.headers.get('Date', '알 수 없음')
print(f"    Date: {date}")
custom = response.headers.get('X-Custom-Header', '존재하지 않음')
print(f"    X-Custom-Header: {custom}")
import requests
import Content_Type_Handling


#과제 1: Header 탐색기
#응답 받아오는 함수 가져왔음 (Content_Type_Handling.py)

urls = [
    "https://httpbin.org/json",   # JSON 응답
    "https://httpbin.org/html",   # HTML 응답
    "https://httpbin.org/xml"    # XML 응답
]

# for url in urls:
#     response = requests.get(url)
#     Content_Type_Handling.handle_response(response)


#과제 2: 사용자 정보 전송
# 보낼 데이터
my_info = {
    "name": "Jaehyun Jimmy Kim",
    "favorite_language": "Python",
    "address": "Seoul"
}

response = requests.post("https://httpbin.org/post", json=my_info)
# 요청했고, 이제 응답 확인

print("=" * 50)
print("Response 정보:")
print(f"  상태 코드: {response.status_code}")
response_data = response.json()
print(f"  서버가 받은 Header : ")
for key, value in response_data['headers'].items():
    print(f"    {key} : {value}")
print(f"  서버가 받은 Body (Json 형태) : ")
print(f"  {response_data['json']}")
#Header 설정을 안해줬는데도, 기본 값으로 들어가서 그런지 Header 정보가 잘 리턴 되었다.

# 과제 3: 에러 응답 분석

# 존재하지 않는 페이지 요청
response = requests.get("https://httpbin.org/status/404")

# 여기에 코드를 작성하세요
# 응답 상태 확인
print("=" * 50)
print(f"Response Status Code : {response.status_code}")
print(f"Response Status Message : {response.reason}")

# 응답 Header 확인
print("=" * 50)
print("Response Header (서버가 보낸 메타데이터):")
print("=" * 50)
    # response.headers : 딕셔너리와 유사한 객체로 반환됨.
for header_name, header_value in response.headers.items():
    print(f"    {header_name}: {header_value}")

# 응답 Body 확인
print("=" * 50)
print("Response Body (서버가 보낸 실제 데이터):")
print("=" * 50)
#응답한 Body를 문자열로 반환
print(response.text)
# 확인할 것:

# 1. 상태 코드가 404인가? 맞음

# 2. 에러 응답에도 Header가 있는가?
#   - 담겨있긴하다.

# 3. Body에는 무엇이 담겨 있는가?
#   - 아무것도 없다.
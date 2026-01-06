#pip install requests

import requests

# 1. GET 요청으로 Header와 Body 확인

"""
HTTP GET 요청 보내기
GET : 서버에서 데이터를 가져오기
"""
# 테스트용 API 서버(httpbin.org)에 GET 요청 보내기
# httpbin.org 사이트는 요청한거 그대로 돌려준다.
response = requests.get("https://httpbin.org/get")

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
# 응답한 Body를 JSON 타입으로 파싱
data = response.json()
print("\n JSON 파싱 결과 : ")
print(f"    요청 URL : {data['url']}")
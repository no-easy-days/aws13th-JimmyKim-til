import requests

def handle_response(response):
    # Content-Type Header 가져오기
    content_type = response.headers.get('Content-Type', '')
    print(f"    Content-Type: {content_type}")
    # JSON 일 경우
    if 'application/json' in content_type:
        print("    json 타입이 검출되어 JSON 형식으로 파싱합니다.")
        return response.json() #딕셔너리
    elif 'text/html' in content_type:
        print("    HTML 타입이 검출되어 HTML 텍스트로 처리합니다.")
        return response.text # 스트링
    elif 'text/plain' in content_type:
        print("    일반 텍스트 타입이 검출되어 텍스트로 처리합니다.")
        return response.text
    else:
        print("    바이너리 데이터로 처리합니다.")
        return response.content #음악, 이미지 파일 등등

print("=" * 50)
print(" Content Type에 따라 다양하게 Response 오는거 확인")
print("=" * 50)

print("1. JSON")
response_1 = requests.get("https://httpbin.org/json")
data_1 = handle_response(response_1)
print(f"    결과 타입: {type(data_1).__name__}")
print("=" * 50)

print("2. HTML")
response_2 = requests.get("https://httpbin.org/html")
data_2 = handle_response(response_2)
print(f"    결과 타입: {type(data_2).__name__}")
print("=" * 50)
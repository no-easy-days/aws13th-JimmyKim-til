import requests
import json
from datetime import datetime

class HTTPAnalyzer:

    """
    <사용 방법>
    analyzer = HTTPAnalyzer()
    analyzer.get("https://example.com")
    analyzer.post("https://api.example.com/data", {"key" : "value"})

    """

    def __init__(self):
        #초기 세팅
        self.default_headers = {
            "User-Agent" : "HTTPAnalyzer/1.0 (by jeff)",
            "Accept" : "application/json, text/html, */*"
        }

    def _print_seperator(self, title):
        #구분선, 제목 출력
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60)

    def _analyze_response(self, response, method):
        #응답 분석 & 정보 출력
        self._print_seperator(f"{method} 요청 정보")
        print(f"    URL : {response.request.url}")
        print(f"    보낸 Header:")
        for header_name, header_value in response.request.headers.items():
            print(f"           {header_name} : {header_value}")

        if response.request.body:
            print(f"    보낸 Body:")
            print(f"           {response.request.body}")

        #응답 정보 출력
        self._print_seperator("응답 정보")
        print(f"    상태: {response.status_code} | {response.reason}")
        print(f"    응답 시간: {response.elapsed.total_seconds():.3f}초")

        #응답 Header 출력
        self._print_seperator("응답 Header")
        for header_name, header_value in response.headers.items():
            print(f"         {header_name} : {header_value}")

        #응답 Body 출력
        self._print_seperator("응답 Body")
        content_type = response.headers.get('Content-Type','') #먼저 받아와서 변수에 로드

        if 'application/json' in content_type:
            try:
                body = json.dumps(
                    response.json(),
                    indent=2,
                    ensure_ascii=False
                )#보기좋게 만들기
                print(body[:500])
                if len(body) > 500:
                    print(" ...(생략)") # 최대 500자 까지 출력하기
            except: # 왜 try except? 프로그램이 터지지 않도록 방어 로직을 짜준거라고 생각하자.
                print(response.text[:500])
        else:
            print(response.text[:500])
            if len(response.text) > 500:
                print(" ...(생략)")

    def get(self, url, headers=None):
        # GET 보내기
        all_headers = {**self.default_headers, **(headers or {})}# 딕셔너리 언패킹
        response = requests.get(url, headers=all_headers)
        self._analyze_response(response, "GET")
        return response


    def post(self, url, data=None, headers=None):
        # GET 보내기
        # 1) url : 요청 URL
        # 2) data : 보낼 데이터 (딕셔너리 형태)
        # 3) headers : 추가 Header (선택사항)
        all_headers = {**self.default_headers, **(headers or {})}  # 딕셔너리 언패킹
        response = requests.post(url, json=data, headers=all_headers)
        self._analyze_response(response, "POST")
        return response


# ========== 사용 예시 ==========
if __name__ == "__main__":
    print("\n" + "#" * 60)
    print("#  HTTP Header/Body 분석 도구 - by jeff (임태종)")
    print("#" * 60)

    analyzer = HTTPAnalyzer()

    # GET 요청 테스트
    print("\n\n🔵 [테스트 1] GET 요청")
    analyzer.get("https://httpbin.org/get")

    # POST 요청 테스트
    print("\n\n🟢 [테스트 2] POST 요청")
    analyzer.post(
        "https://httpbin.org/post",
        data={
            "instructor": "jeff",
            "course": "HTTP Header/Body",
            "students": 30
        }
    )
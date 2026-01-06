from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #/api/user 경로로 요청받으면
        if self.path == '/api/user':
        # JSON으로 응답
            data = {"name" : "김재현", "nickname" : "Jimmy", "role" : "Student"}

            #Response Header 작성 - "영수증"
            self.send_response(200) # status code 전달
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            #Responce Body 작성
            self.wfile.write(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))

        else:
            self.send_response(404) # status code 전달 - 클라이언트 에러
            self.end_headers()

if __name__== '__main__':
    # 서버 Address, Port 초기화
    server_address = ('', 8000)

    # 서버 생성
    httpd = HTTPServer(server_address, MyHandler) #MyHandler 클래스 객체 받음


    print(f"🚀 Server is running on port 8000...")
    print(f"   (http://localhost:8000/api/user) 로 접속해보세요.")

    # 서버 실행 및 대기 (손님이 올 때까지 무한 대기)
    httpd.serve_forever()
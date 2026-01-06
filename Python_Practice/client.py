import requests
# pip 설치해야함!

# 1. 요청 보낼 목적지 설정 (서버 주소)
url = 'http://localhost:8000/api/user'

print(f"📡 요청 보내는 중... : {url}")

# 2. GET 요청 전송 (주문 하기)
try:
    response = requests.get(url)

    # 3. 응답 확인 (음식 받기)
    print(f"✅ 상태 코드: {response.status_code}")  # 200이면 성공
    print(f"📦 응답 데이터: {response.json()}")  # 받은 데이터 확인

except Exception as e:
    print(f"❌ 연결 실패: {e}")
    print("서버가 켜져 있는지 확인해주세요!")
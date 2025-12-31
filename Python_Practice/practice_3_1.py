#실습 3-1: 이메일 주소 분리하기
email_address = input("이메일 주소를 입력하세요... : ")
print(f"사용자 이름: {email_address.split('@')[0]}")
print(f"도메인: {email_address.split('@')[1]}")

#실습 3-2: 비밀번호 길이 검사
password = input("사용할 비밀번호를 입력하세요... : ")
if len(password) >= 8:
    print(f"유효한 비밀번호입니다. ")
else:
    print(f"비밀번호가 8자리 이하입니다. 다시 만드세요.")

#실습 3-3: 3의 배수 찾기
result_list = []
for i in range(1, 21):
    if i % 3 == 0:
        result_list.append(i)
    else:
        continue
print(f"결과 리스트 값 : {result_list}")

#실습 3-4: 공통 관심사 찾기
chulsoo = ["축구", "영화", "음악", "게임", "독서"]
younghee = ["영화", "음악", "요리", "여행", "독서"]
common_interest = []
for i in chulsoo:
    if i in younghee:
        common_interest.append(i)
print(f"공통 관심사 : {common_interest}")
# 정답에서는 set의 교집합(&) 을 활용했다. 그게 더 간결한 것 같다.

#실습 3-5: 최고 점수 학생 찾기
scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88
}
max_name = ""
max_score = 0
print(f"{scores.items()}")
for i, j in scores.items():
    if j > max_score:
        max_score = j
        max_name = i
print(f"제일 잘한 학생 : {max_name} 이고, 점수는 {max_score}")
# 엇비슷한듯?

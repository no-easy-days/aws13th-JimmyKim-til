# 실습 1 : 변수 선언 (기초)
my_name = "김재현"
my_age = 32
my_favorite_number = 1108
print(f"이름 : {my_name}, 나이 : {my_age}, 좋아하는 숫자 : {my_favorite_number}")

# 실습 2 : 값 교환 (기초)
first = "A"
second = "B"
first, second = second, first
print(f"값 교환 결과 => first : {first}, second : {second}")

# 실습 3 : 복합 연산 (기초)
balance = 10000
balance = (balance - 3000) * 2
print(f"최종 값 : {balance}")

# 실습 4 : 오류 수정 (응용)
"""
< 원본 코드 >
2nd_place = "은메달"
user name = "홍길동"
class = "1학년"
"""
second_place = "은메달" # 변수는 숫자로 시작할 수 없다.
user_name = "홍길동" # 변수에 공백은 들어갈 수 없다.
class_grade = "1학년" # class는 예약어

# 실습 5 : 자료형 확인하기 (기초)
print(type(42))
print(type(3.14))
print(type("Hello"))
print(type(True))
print(type(None))

# 실습 6 : 형변환 연습 (기초)
# prac6_A = input("첫번째 숫자를 입력하세요 : ")
# prac6_B = input("두번째 숫자를 입력하세요 : ")
# print(f"두 숫자의 합은 {int(prac6_A)+int(prac6_B)} 입니다.")

# 실습 7 : 자기소개 프로그램 (응용)
# user_name = input("사용자의 이름을 입력하세요 : ")
# user_age = input("사용자의 나이를 입력하세요 : ")
# user_height = input("사용자의 키를 입력하세요 : ")
# print(f"""
#     안녕하세요! 제 이름은 {user_name}입니다.
#     나이는 {user_age}살이고, 내년에는 {str(int(user_age)+1)}살이 됩니다.
#     제 키는 {user_height}cm 입니다.
#     """)

# 실습 8 : 계산기 만들기 (심화)
prac8_num1 = input("첫번째 숫자를 입력하세요 : ")
prac8_num2 = input("두번째 숫자를 입력하세요 : ")
prac8_oper = input("원하는 연산자를 입력하세요 : ")
prac8_result = ""
if prac8_oper == "+":
    prac8_result = float(prac8_num1) + float(prac8_num2)
elif prac8_oper == "-":
    prac8_result = float(prac8_num1) - float(prac8_num2)
elif prac8_oper == "*":
    prac8_result = float(prac8_num1) * float(prac8_num2)
elif prac8_oper == "%":
    if prac8_num2 == 0:
        print(f"0으로 나누면 나머지를 구할 수 없습니다. ")
        raise ZeroDivisionError
    prac8_result = float(prac8_num1) % float(prac8_num2)
elif prac8_oper == "/":
    prac8_result = float(prac8_num1) / float(prac8_num2)
    if prac8_num2 == 0:
        print(f"0으로 나눗셈을 할 수 없습니다. ")
        raise ZeroDivisionError
elif prac8_oper == "//":
    prac8_result = float(prac8_num1) // float(prac8_num2)
    if prac8_num2 == 0:
        print(f"0으로 나누면 몫을 구할 수 없습니다. ")
        raise ZeroDivisionError
else:
    print(f"오류가 발생했습니다. 지원하지 않는 연산자입니다. ")
    raise ValueError

# 피드백 반영 --- 2026.01.06
# 1. 방어 로직 구현하기 (잘못된 연산자 검출)
# 2. 제로 나누기 예외 처리


print(f"계산 결과 : {prac8_num1} {prac8_oper} {prac8_num2} = {prac8_result}")

# 해설을 보니, 0으로 나누는 경우 예외처리 / 잘못된 연산자를 입력한 경우 예외처리 두가지가 있었다.
# Pycharm에서 Git 연동해서 Push 테스트를 진행하자. 왜 안되지?
# token 활용 테스트
# 실습 1:  계산기 함수
def calculator(a, b, operator):
    operator_example = ["+", "-", "*", "/"]
    if operator == operator_example[0]:
        return a + b
    elif operator == operator_example[1]:
        return a - b
    elif operator == operator_example[2]:
        return a * b
    elif operator == operator_example[3]:
        if b == 0:
            return "0으로 나눌 수 없습니다."
        return a / b
    elif operator not in operator_example:
        return "지원하지 않는 연산자입니다."

# 피드백 내용 구현(람다식 활용) -- 2026.01.06
def calculator_lambda(a, b, operator):
    # 딕셔너리 자료형을 선언하고, 연산자를 키값으로 받아서 결과값을 람다식으로 반환하네.
    # 창의적이다...
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else "0으로 나눌 수 없습니다"
    }
    result = operations.get(operator)

    if result is None:
        return "지원하지 않는 연산자입니다"
    return result(a, b)

print(calculator_lambda(10,5,'+'))
print(calculator(10, 5, '+'))  # 15
print(calculator(10, 5, '-'))  # 5
print(calculator(10, 5, '*'))  # 50
print(calculator(10, 5, '/'))  # 2.0
print(calculator(10, 0, '/'))  # 0으로 나눌 수 없습니다
print(calculator(10, 5, '%'))  # 지원하지 않는 연산자입니다

# 실습 5-2: 학생 성적 처리
def print_report(name, scores):
    print(f"=== {name} 성적표 ===")
    print(f"점수 : {scores}")
    print(f"평균 : {sum(scores) / len(scores)}점")
    print(f"최고점 : {max(scores)}점")
    print(f"최저점 : {min(scores)}점")
    avg = sum(scores) / len(scores)
    if avg >= 90:
        print(f"등급: A")
    elif avg >= 80:
        print(f"등급: B")
    elif avg >= 70:
        print(f"등급: C")
    elif avg >= 60:
        print(f"등급: D")
    else:
        print(f"등급: F")

print_report("김철수", [85, 92, 78, 96, 88])
# 풀이에서, 평균을 낼 때 avg:.1f 를 썼다. 소수점 첫번째까지만 출력하도록 설정했다.

# 실습 5-3: 비밀번호 검증
def validate_password(password):
    if len(password) < 8:
        return (False, "8자 이상이어야 합니다")

    # has_digit = False
    # for char in password:
    #     if char.isdigit():
    #         has_digit = True
    #         break

    # 피드백 내용 반영 -- 2026.01.05
    # 제너레이터 표현식 & any를 활용하였다.
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return (False, "숫자를 포함해야 합니다")

    # 조건 3: 대문자 포함
    # has_upper = False
    # for char in password:
    #     if char.isupper():
    #         has_upper = True
    #         break

    # 피드백 내용 반영 -- 2026.01.05
    # 제너레이터 표현식 & any를 활용하였다.
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        return (False, "대문자를 포함해야 합니다")

    # 모든 조건 통과
    return (True, "유효한 비밀번호입니다")
# 훨씬 간결해졌다.

print(validate_password("abc"))        # (False, "8자 이상이어야 합니다")
print(validate_password("abcdefgh"))   # (False, "숫자를 포함해야 합니다")
print(validate_password("abcdefg1"))   # (False, "대문자를 포함해야 합니다")
print(validate_password("Abcdefg1"))   # (True, "유효한 비밀번호입니다")

# 심화 주제 풀고 오니 굉장히 쉬워졌다.
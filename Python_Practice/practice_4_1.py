import random #실습4-4를 위해

# 실습 4-1: 등급 판정
# score = int(input("점수를 입력하세요: "))
# if score in range(1, 101):
#     if score >= 90:
#         print(f"등급 : A")
#     elif score >= 80:
#         print(f"등급 : B")
#     elif score >= 70:
#         print(f"등급 : C")
#     elif score >= 60:
#         print(f"등급 : D")
#     else:
#         print(f"등급 : F")
# else:
#     print(f"잘못된 입력입니다.")
# 풀이 : range 쓰지 않고 연산자 사용.

# 실습 4-2: 구구단 출력
# prac2_num = int(input("몇 단을 할까요? : "))
# print(f"=== {prac2_num}단 ===")
# for i in range(1, 10):
#     print(f"{prac2_num} X {i} = {prac2_num*i}")
# 풀이 : 유효성 검사를 넣었다. 넣어주는게 좋을 것 같다.

# 실습 4-3: 소수 판별
prime_number = ""

for i in range(2, 101):
    is_prime_number = True

    for j in range(2, i):
        if i % j == 0:
            is_prime_number = False
            break

    if is_prime_number:
        prime_number = prime_number + str(i) + " "

print(prime_number)
# 풀이 : 엇비슷한데.. 접근 방법은 맞은듯?

#실습 4-4: 숫자 맞추기 게임
answer = random.randint(1,100)
count = 1
print(f"1부터 100까지의 난수가 뭐였는지를 찾아봅시다.")

while answer: # 풀이에서는 True로 받았다. 그냥 계속 반복 시킬때는 True 쓰면 될듯.
    guess = input("숫자를 입력하세요... : ")

    if guess == '': #풀이에는 굳이 안해줬는데... 일단 나는 넣어줌.
        print(f"공백이 입력되었습니다. 다시 입력해주세요")
        continue
    elif int(guess) > answer:
        print(f"더 작은 수를 입력하세요. ")
        count += 1
        continue
    elif int(guess) < answer:
        print(f"더 큰 수를 입력하세요. ")
        count += 1
        continue
    else:
        print(f"정답입니다! {count}번 만에 맞추셨습니다!")
        break
#풀이랑 흐름은 비슷한듯? 접근법은 틀리진 않았나보다.
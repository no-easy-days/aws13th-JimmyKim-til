# 실습 1: 1부터 n까지 합계
def sum_to_n(n):
    #여기에 코드를 작성하세요
    if n == 1:
        return 1
    elif n == 0:
        return  0
    else:
        return n + sum_to_n(n-1)

print(sum_to_n(5))   # 15 (1+2+3+4+5)
print(sum_to_n(10))  # 55 (1+2+3+...+10)
print(sum_to_n(1))   # 1

# 실습 2: 거듭제곱
def power(x, n):
    # 여기에 코드 작성
    if x == 1 or n == 0:
        return 1
    elif x > 1:
        return x * power(x, n-1)

print(power(2, 3))   # 8  (2³ = 2×2×2)
print(power(5, 2))   # 25 (5² = 5×5)
print(power(3, 0))   # 1  (모든 수의 0제곱은 1)
print(power(1,0))

# 실습 3: 문자열 뒤집기
def reverse_string(s):
#    if s == "":
#        return "" ---> 이렇게 하면 한 글자 일때 기저조건 달성ㅇ ㅣ안됨.
    if len(s) <= 1:
        return s
    return s[len(s)-1] + reverse_string(s[:-1])
#   return reverse_string(s[1:]) + s[0]
    # 나는 마지막 스트링을 뽑아내고 그 뒤에 재귀를 넣었는데,
    # 풀이에서는 재귀를 먼저 하고 제일 첫 스트링을 부여했다.

print(reverse_string("hello"))   # "olleh"
print(reverse_string("python"))  # "nohtyp"
print(reverse_string("a"))       # "a"
print(reverse_string(""))        # ""`
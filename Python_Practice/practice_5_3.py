# 실습 1: 할인 계산기
def make_discounter(discount_rate):
    def discounted_price(target_price): # 중첩 함수 정의
        return target_price - (target_price * discount_rate) #외부 변수 참조
    return discounted_price # 내부 함수 반환

ten_percent_off = make_discounter(0.1)   # 10% 할인
half_off = make_discounter(0.5)          # 50% 할인

print(ten_percent_off(10000))  # 9000
print(half_off(10000))         # 5000

# 실습 2: 호출 횟수 카운터

def make_counter_func(func):
    def count_number(*args, **kwargs):
        count_number.count += 1
        return func(*args, **kwargs)

    count_number.count = 0
    return count_number

def say_hello():
    print("Hello!")

counted_hello = make_counter_func(say_hello)
counted_hello()  # Hello!
counted_hello()  # Hello!
counted_hello()  # Hello!
print(f"호출 횟수: {counted_hello.count}")  # 호출 횟수: 3
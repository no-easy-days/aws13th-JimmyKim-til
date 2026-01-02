import functools
import time

def decorator_example(function):  # 호출할 함수를 매개변수로 받음
    def wrapper():  # 호출할 함수를 감싸는 함수
        print("wrapper 함수가 시작되었습니다. 내부의 원본함수를 불러옵니다.")
        function()  # 매개변수로 받은 함수를 호출
        print("원본함수가 실행 완료 되었습니다. wrapper를 리턴합니다.")
    return wrapper

@decorator_example
def greetings():
    print("Hello World!")

greetings() # 결과를 보면, 실제 Hello World 수행 앞 뒤로 쟤네들이 실행됨.

# 시간 측정 예제

def timer(function):
    print(f"데코레이터 시작.{function.__name__}을 wrapper로 감싼다. ")

    def wrapper(*args, **kwargs):
        print(f"시간 측정 시작... wrapper 시작")
        start = time.time() #원본 함수 실행 "전"
        print(f"원본함수 호출 직전입니다. 시간 측정 시작했고 원본함수 호출합니다.")

        result = function(*args, **kwargs) # 원본 함수 호출

        end = time.time() #원본 함수 실행 "후"
        print(f"원본함수 호출 완료입니다. 실행시간은 : {end - start:.4f}초")
        return result

    return wrapper

@timer
def slow_function():
    print("원본 함수 차례입니다. 슬립 0.5 줘봅니다...")
    time.sleep(0.5)
    return "완료"

result = slow_function()
print(f"결과 : {result}, 실제 실행 시간은 wrapper에 찍도록 해둬서 그전에 찍힙니다.")

# 실습 1: 함수 호출 횟수 세보기
def count_calls(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        wrapper.call_count = wrapper.call_count + 1
        print(f"wrapper 확인해보겠습니다. {wrapper.call_count}번 호출됨")
        return function(*args, **kwargs)

    wrapper.call_count = 0 # 함수에 변수를 붙여서 상태를 저장할 수 있음.
    return wrapper

@count_calls
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()
print(say_hello.call_count)

# 실습 2: 결과 캐싱 (메모이제이션)
def cache(function):
    cached_results = {} # 캐시 저장소 선언. dictionary
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cached_results:
            print(f"캐시에서 반환 : {key}")
            return cached_results[key]

        print(f"새로 계산하면 : {key}")
        result = function(*args, **kwargs)
        cached_results[key] = result
        return result
    return wrapper

    wrapper.clear_cache = lambda: cashed_results.clear()
    wrapper.cache = cached_results

@cache
def slow_add(a, b):
    import time
    time.sleep(1)  # 느린 연산 시뮬레이션
    return a + b

print(slow_add(1, 2))  # 1초 후 3
print(slow_add(1, 2))  # 즉시 3 (캐시에서 반환)
print(slow_add(3, 4))  # 1초 후 7
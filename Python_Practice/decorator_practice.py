def trace(func):  # 호출할 함수를 매개변수로 받음
    def wrapper():  # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')

    return wrapper  # wrapper 함수 반환

#중요한 포인트는, wrapper를 "실행하지 않고, 만들어서 반환"

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')

hello()
world()

trace_hello = trace(hello)  # 데코레이터에 호출할 함수를 넣음
trace_hello()  # 반환된 함수를 호출
trace_world = trace(world)  # 데코레이터에 호출할 함수를 넣음
trace_world()  # 반환된 함수를 호출
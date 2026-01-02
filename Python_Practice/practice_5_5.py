# 실습 1: 온도 변환

celsius = [0, 10, 20, 30, 40]
# map()을 사용하여 화씨로 변환
fahrenheit = list(map(lambda x : x * 9/5 + 32, celsius))
print(fahrenheit)

# 실습 2: 성인 필터링
people = [
    {"name": "김철수", "age": 25},
    {"name": "이영희", "age": 17},
    {"name": "박민수", "age": 30},
    {"name": "최지영", "age": 15},
    {"name": "정동훈", "age": 22}
]
# filter()를 사용하여 성인만 추출 (19세 이상)
adults = list(filter(lambda x : x["age"] >= 19, people))
print(adults)

# 실습 3: 복합 조건
numbers = [-4, 16, -9, 25, 0, 36, -1, 49]
# filter()와 map()을 조합하여 양수의 제곱근 구하기
result = list(map(lambda x : abs(x) ** 0.5, list(filter(lambda x : x > 0, numbers))))
print(result)  # [4.0, 5.0, 6.0, 7.0]

# 실습 4: 리스트 컴프리헨션으로 변환
words = ["hello", "world", "python", "ai", "map"]
# 원본 코드 (map + filter)
result = list(map(str.upper, filter(lambda w: len(w) > 3, words)))
print(result) # ['HELLO', 'WORLD', 'PYTHON']
# 리스트 컴프리헨션으로 변환
result_comp = [i.upper() for i in words if len(i) > 3]
print(result_comp)

# 추가 연습 A : map/filter 와 리스트 컴프리헨션 연습하기 1
words = ["apple", "cat", "banana", "dog", "elephant"]
# 결과: ['a', 'b', 'e']
result_mapfilter = list(map(lambda x : x[0], list(filter(lambda x : len(x) >= 5, words))))
print(result_mapfilter)
result_listCom = [x[0] for x in words if len(x) >= 5]
print(result_listCom)

# 추가 연습 B : map/filter 와 리스트 컴프리헨션 연습하기 2
numbers = [1, 3, 5, 6, 9, 11, 12, 15]
# 결과: [13, 16, 19, 22, 25]
resultB_mapfilter = list(map(lambda x : x + 10, list(filter(lambda x : x%3 == 0, numbers))))
print(resultB_mapfilter)
resultB_listCom = [x+10 for x in numbers if x % 3 == 0]
print(resultB_listCom)
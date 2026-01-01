# 실습 1: 정렬하기

cities = [
    {"name": "서울", "population": 9700000},
    {"name": "부산", "population": 3400000},
    {"name": "인천", "population": 2900000},
    {"name": "대구", "population": 2400000}
]

# 인구수 오름차순 정렬
sorted_cities = sorted(cities, key=lambda x : x["population"])

# 결과: [대구, 인천, 부산, 서울]
print([i["name"] for i in sorted_cities]) # 리스트 컴프리헨션

# 실습 2: 데이터 변환

str_numbers = ["10", "20", "30", "40", "50"]
# 1단계: 정수로 변환
result = list(map(lambda x :int(x), str_numbers))
#print(result)... X, "메모리 주소"만 반환한다. list 자료형으로 변환해야한다.
# 2단계: 100 더하기
final_result = list(map(lambda x : x+100, result))
# 결과: [110, 120, 130, 140, 150]
print(final_result)

#한번의 람다에서 동시에 처리해보기
final_result2 = list(map(lambda x : int(x)+100, str_numbers))
print(final_result2)

# 실습 3 : 필터링
products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]
# 할인율 20% 이상만 추출
discounted = list(filter(lambda x : x["discount"]>20, products))
# 결과: [{'name': '마우스', 'discount': 25}, {'name': '키보드', 'discount': 30}]
print(discounted)
# 리스트 컴프리헨션 한번 써보면
print([i for i in products if i["discount"] > 20])

# 추가 연습 문제 A
students = [
    {"name": "김철수", "score": 88},
    {"name": "이영희", "score": 95},
    {"name": "박민수", "score": 72}
]
# 힌트: max()의 key 인자 사용
max_score_student = max(students, key=lambda x : x["score"])
print(max_score_student["name"])

# 추가 연습 문제 B
words = ["apple", "cat", "banana", "elephant", "dog"]
# 힌트: sorted()의 key에 len 함수 사용
sorted_words = sorted(words, key=lambda x : len(x), reverse=True)
print(sorted_words)
import csv
import json
#csv, json파일 저장 경로 설정
file_path = "C:/AWS13th_JimmyKim/TIL/aws13th-JimmyKim-til/Python_Practice/target_file"

# 실습 1: csv 읽기 (기본)
with open(file_path+"/users.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['이름']} - {row['직업']}")
    f.close()

# 실습 2: csv 필터링
with open(file_path+"/users.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['나이']) >= 30:
            print(f"{row['이름']} ({row['나이']}세)")
    f.close()

# 실습 3: csv 쓰기
students = [
{'학번': 'S001', '이름': '김민수', '학과': '컴퓨터공학'},
{'학번': 'S002', '이름': '이수진', '학과': '전자공학'},
{'학번': 'S003', '이름': '박영호', '학과': '기계공학'},
]
with open(file_path + "/students.csv", 'w', encoding='utf-8') as f:
    print(students[0].keys()) #리스트로 변환해두는 것이 안전할 듯
    writer = csv.DictWriter(f, fieldnames=list(students[0].keys()))
    writer.writeheader()  # 헤더 쓰기
    writer.writerows(students)  # 데이터 쓰기
    f.close()

# 실습 4: json 읽기 (기본)
with open(file_path + "/config.json", 'r', encoding='utf-8') as f:
    load = json.load(f)
    print(f"앱 이름 : {load['app_name']}")
    print(f"앱 버전 : {load['version']}")
    print(f"DB 호스트 : {load['database']['host']}") # 딕셔너리 체이닝!
    f.close()

# 실습 5: json 수정 및 저장
with open(file_path + "/config.json", 'r', encoding='utf-8') as f:
    load = json.load(f)
    # 값 변경 시작
    load['debug'] = True
    load['features'].append("notifications")
    print(load) #결과 확인
    with open(file_path + "/config_updated.json", 'w', encoding='utf-8') as d:
        json.dump(load, d, ensure_ascii=False, indent=2)
    f.close()
    d.close()

# 실습 6: csv > json 변환
with open(file_path + "/users.csv", 'r', encoding='utf-8') as f:
    reader = list(csv.DictReader(f))
    print(reader)
    with open(file_path + "/users.json", 'w', encoding='utf-8') as d:
        json.dump(reader, d, ensure_ascii=False, indent=2)
        d.close()
    f.close()
# 나는 with open 밑에 중첩해서 햇는데, 생각해보니 프로그램이 끝난게 아니니까 close 하고 다시 해도 될듯

# 실습 7: 실무 시나리오 - 로그 분석
#1. logs.json 파일 먼저 만들기
test_log = [
    {"timestamp": "2025-01-01 10:00:00", "level": "INFO", "message": "서버 시작"},
    {"timestamp": "2025-01-01 10:05:00", "level": "ERROR", "message": "DB 연결 실패"},
    {"timestamp": "2025-01-01 10:10:00", "level": "INFO", "message": "재연결 시도"},
    {"timestamp": "2025-01-01 10:15:00", "level": "ERROR", "message": "타임아웃 발생"},
    {"timestamp": "2025-01-01 10:20:00", "level": "INFO", "message": "정상 복구"}
]
with open(file_path + "/logs.json", 'w', encoding='utf-8') as f:
    json.dump(test_log, f, ensure_ascii=False, indent=2)
    f.close()

errors = [] # 에러발생한 로그들을 리스트 형태로 저장하기 위해 초기화

with open(file_path + "/logs.json", 'r', encoding='utf-8') as f:
    load = json.load(f)
    for i in load:
        if i['level'] == "ERROR":
            errors.append(i)

with open(file_path + "/errors.json", 'w', encoding='utf-8') as f:
    json.dump(errors, f, ensure_ascii=False, indent=2)
    f.close()
# 풀이에서는 리스트 컴프리헨션으로 간단하게 표현했다. 좀 더 익숙해져야겠다.
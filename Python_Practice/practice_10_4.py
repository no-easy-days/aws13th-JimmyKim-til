# [실습 10.1-1] 위험한 코드 찾기

name = input("이름: ")
age = input("나이: ")

#sql = f"INSERT INTO students VALUES ('{name}', {age})"
#cursor.execute(sql)

"""
위험한 이유?
    - input을 통해 받은 사용자 입력값을 그대로 SQL 문에 끼워 넣고 있다.
    - name 또는 age 이후에 DROP SQL 문 삽입 하면 테이블 날릴 수 있음.

# 풀이)
    - f-string으로 사용자 입력을 직접 SQL 문에 삽입하기 때문에.
    - 입력값 name, age 모두 별도의 검증 과정 없이 그대로 사용.

"""

# [실습 10.1-2] 안전한 코드로 수정하기

name = input("이름: ")
age = input("나이: ")
# Placeholder 활용
# 피드백 반영 -- 2026.01.06 %d는 정수형!
sql = "INSERT INTO students VALUES (%s, %s)"
cursor.execute(sql, (name, age))
# Placeholder 이름 기반 %(key)s 활용
sql = "INSERT INTO students VALUES (%(name)s, %(age)s)"
cursor.execute(sql, {"name" : name, "age" : age})

# [실습 10.1-3] 공격 시나리오 분석
product_name = input("검색할 상품: ")
sql = f"SELECT * FROM products WHERE name = '{product_name}'"

"""
모든 상품 정보를 볼 수 있는 입력 값?
    - name 입력값 뒤에  ' OR '1'='1' 추가.
"""

#[도전 10.1-4] 이름 기반 Placeholder 활용
# 위험한 코드
keyword = input("검색어: ")
sql = f"""
    SELECT * FROM posts 
    WHERE title LIKE %(kw)s 
    OR content LIKE %(kw)s
    OR author LIKE %(kw)s
"""
cursor.execute(sql, {"kw" : f"%{keyword}%"})

#교안 보고 따라 작성하긴 했는데, 활용도는 잘 모르겠다...


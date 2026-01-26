import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

# 1. DB 연결
conn = pymysql.connect(
     host=os.getenv('DB_HOST'),
     port=int(os.getenv('DB_PORT')),
     user=os.getenv('DB_USER'),
     db=os.getenv('DB'),
     password=os.getenv('DB_PASSWORD'),
     charset='utf8mb4'
)

print("연결 성공!")
# 2. 커서 생성

cursor = conn.cursor()

# 3. SQL 실행
cursor.execute("SELECT * FROM members")

# 4. 결과 가져오기
rows = cursor.fetchall()
for row in rows:
    print(row)

# 5. 종료 (커서 → 연결 순서)
cursor.close()
conn.close()
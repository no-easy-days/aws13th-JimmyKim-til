# 실습 1: import 기본 사용
import datetime
today = datetime.date.today()
print(today)

# 실습 2: from import 사용
from math import sqrt, pow
print(sqrt(16))
print(pow(2,10))

# 실습 3: 별명(as) 사용
import random as rd
print(rd.randint(1,100))

# 실습 4: pip 명령어
# 터미널에서 명령어 치면 된다.
# pip install, pip list
# pip freeze > 타겟파일명.txt

# 실습 5: 가상환경 명령어
# 터미널에서 명령어 치면 된다.
# python -m venv venv, 활성화: venv\Scripts\activate, 비활성화: deactivate

# 실습 6: 실무 시나리오
# 명령어 작성
"""
1) mkdir weather_app
2) cd weather_app
3) python -m venv venv
4) venv\Scripts\activate
5) pip install requests
6) pip install python-dotenv
7) pip freeze > requirements.txt
"""

# 도전 문제: 팀원에게 프로젝트 공유하기
# 명령어 작성
"""
1) python -m venv venv (가상 환경은 일단 만들어야함)
2) venv\Scripts\activate
3) pip install -r requirements.txt
"""
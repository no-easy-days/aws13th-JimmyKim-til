from dataclasses import dataclass

# 실습 1: 기본 클래스 만들기
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def introduce(self):
        print(f"안녕하세요, {self.grade}학년 {self.name}입니다. (학번 : {self.student_id})")

kim = Student("김철수", "2024001", 1)
kim.introduce()
# 출력: 안녕하세요, 1학년 김철수입니다. (학번: 2024001)

# 실습 2: 상태 관리하기
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"잔액이 부족합니다. ")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

account = BankAccount("김재현")
account.deposit(10000)
account.withdraw(3000)
print(account.get_balance())  # 7000
account.withdraw(10000)  # 잔액이 부족합니다

# 실습 3: 리스트 속성 관리하기
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
    # 풀이 : 그 할일이 tasks에 이미 있는지를 확인하는게 좋긴하겠다.
        if task in self.tasks:
            self.tasks.remove(task)

    def show_tasks(self):
    # 풀이 : 예시 처럼 나와야 해서 순번을 부여해주자.
        print(f"---해야하는 Todo_list---")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}번 : {task}")
#        print(f"{self.tasks}")

my_todo = TodoList()
my_todo.add_task("Python 공부")
my_todo.add_task("Git 연습")
my_todo.show_tasks()
my_todo.complete_task("Python 공부")
my_todo.show_tasks()

# 실습 4: 실무 스타일 - dataclass 사용하기

@dataclass
class DatabaseConfig:
    host : str
    port : int
    username : str
    password : str
    database : str
    timeout : int = 30
    pool_size : int = 5

config = DatabaseConfig(
    host="[localhost]",
    port=3306,
    username="admin",
    password="secret123",
    database="myapp"
)
print(config)

# 도전 문제: EC2 인스턴스 매니저
class EC2Instance:
    def __init__(self, instance_id, name):
        self.instance_id = instance_id
        self.name = name
        self.status = "stopped"

    def start(self):
        self.status = "started"

    def stop(self):
        self.status = "stopped"

class EC2Manager:
    def __init__(self):
        self.instances = []

    def add_instance(self, instance):
        self.instances.append(instance)

    def start_all(self):
        for instance in self.instances:
            instance.start()

    def  stop_all(self):
        for instance in self.instances:
            instance.stop()

    def get_running_count(self):
        started_instance_cnt = 0
        for instance in self.instances:
            if instance.status == "started":
                started_instance_cnt += 1
        return started_instance_cnt

# 인스턴스 생성
web = EC2Instance("i-001", "web-server")
db = EC2Instance("i-002", "db-server")
cache = EC2Instance("i-003", "cache-server")

# 매니저에 등록
manager = EC2Manager()
manager.add_instance(web)
manager.add_instance(db)
manager.add_instance(cache)

# 모두 시작
manager.start_all()
print(manager.get_running_count())  # 3

# 일부 중지
db.stop()
print(manager.get_running_count())  # 2
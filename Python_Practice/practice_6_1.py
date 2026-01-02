# 실습 1: 탈 것 클래스
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} : 이동")

class Car(Vehicle):
    def move(self): #메서드 오버라이딩
        print(f"{self.name} : 도로를 달립니다.")

class Airplane(Vehicle):
    def move(self):
        print(f"{self.name} : 하늘을 납니다.")

car = Car("자동차")
airplane = Airplane("비행기")
car.move()
airplane.move()

# 실습 2: 학생 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"안녕하세요 제 이름은 {self.name}, 나이는 {self.age} 입니다.")

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age) # 부모 클래스 받아와서 속성 추가하기.
        self.school = school

    def introduce(self):
        print(f"저는 {self.school} 에 다니는 {self.name} 입니다.")


person = Person("김재현", 30)
student = Student("김재현", 30, "부산남일고")
person.introduce()
student.introduce()


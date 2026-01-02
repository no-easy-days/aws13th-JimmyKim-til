# 실습 1: 클래스 변수 활용
# 요구사항:
# - 클래스 변수: total_accounts (총 계좌 수)
# - 인스턴스 변수: owner (소유자), balance (잔액)
# - 계좌가 생성될 때마다 total_accounts가 1 증가
class BankAccount:
    total_accounts = 0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

        BankAccount.total_accounts += 1

# 예상 결과:
a1 = BankAccount("김철수", 10000)
a2 = BankAccount("이영희", 20000)
print(BankAccount.total_accounts) # 예상 결과 : 2

# 실습 2 : 포함관계 설계
# 요구사항:
# - Book: title, author 속성
# - Library: name 속성, books 리스트
# - Library에 add_book(), list_books() 메서드 구현

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"{self.name} 보유 도서 : ")
        if self.books == "":
            print(f"보유 도서가 없습니다. ")
            return
        for book in self.books:
            print(f"- {book.title} ({book.author})")

lib = Library("중앙도서관")
lib.add_book(Book("파이썬 기초", "홍길동"))
lib.add_book(Book("클린 코드", "로버트 마틴"))
lib.list_books()
# 중앙도서관 보유 도서:
# - 파이썬 기초 (홍길동)
# - 클린 코드 (로버트 마틴)

# 풀이에서는 __str__ 사용해서 print 찍을 떄 패턴 그대로 찍도록 했음.

# 실습 3: 특별 메서드 구현
# 요구사항:
# - amount 속성
# - __add__: 금액 더하기
# - __eq__: 금액 비교 (==)
# - __lt__: 금액 비교 (<)
# - __str__: "10,000원" 형태로 출력

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, target):
        if isinstance(target, Money):
            return Money(self.amount + target.amount)
        elif isinstance(target, (int, float)):
            return Money(self.amount + target)
        return NotImplemented

    def __radd__(self, other):
        """역방향 +: 숫자 + Money"""
        return self.__add__(other)

    def __sub__(self, other):
        """- 연산자"""
        if isinstance(other, Money):
            return Money(self.amount - other.amount)
        return NotImplemented

    def __eq__(self, other):
        """== 비교"""
        if isinstance(other, Money):
            return self.amount == other.amount
        return False

    def __lt__(self, other):
        """< 비교"""
        if isinstance(other, Money):
            return self.amount < other.amount
        return NotImplemented

    def __le__(self, other):
        """<= 비교"""
        return self == other or self < other

    def __gt__(self, other):
        """> 비교"""
        if isinstance(other, Money):
            return self.amount > other.amount
        return NotImplemented

    def __ge__(self, other):
        """>= 비교"""
        return self == other or self > other

    def __str__(self):
        """문자열 표현: 천 단위 콤마 + '원'"""
        return f"{self.amount:,}원"

    def __repr__(self):
        """개발자용 표현"""
        return f"Money({self.amount})"

m1 = Money(5000)
m2 = Money(3000)
m3 = m1 + m2
print(m3)  # 8,000원
print(m1 > m2)  # True
print(m1 == m2)  # False
print(m1 < m2)  # False
m4 = m1 - m2
print(m4)  # 2,000원

# 이건 너무 어렵다... 넘어가고 다시 공부해보자 ㅠㅠ
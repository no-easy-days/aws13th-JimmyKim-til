from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, Session, relationship

#=======================================================
#1. 데이터베이스 엔진 생성 ---- 2026.01.26 IP 정보 숨기기
#=======================================================
engine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/orm_practice",
    echo=True
)

#=======================================================
#2. ORM Base 생성
#=======================================================
orm_base = declarative_base()

#=======================================================
#3. 1:N 관계 모델 정의 예시
#=======================================================
class Team(orm_base):
    __tablename__ = 'teams'
    team_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    # 1:N, Team은 1쪽이고 N쪽을 참조한다.
    members = relationship('Member', back_populates='team')
    # 디버깅용 객체 문자열 출력을 위한 매직 메서드
    def __repr__(self):
        return f"<Team(team_id={self.team_id}, name='{self.name}>"

class Member(orm_base):
    __tablename__ = 'members'
    member_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    # 외래키는 항상 N쪽에 존재한다.
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    # N:1, Memeber는 N쪽이고 1쪽을 참조한다.
    team = relationship('Team', back_populates='members')
    # 디버깅용 객체 문자열 출력을 위한 매직 메서드
    def __repr__(self):
        return f"<Member(member_id={self.member_id}, name='{self.name}>"

#=======================================================
#4. 1:N 관계 모델 테스트 모듈
#=======================================================
def test_one_to_N():
# 테이블 생성
    orm_base.metadata.create_all(engine)
    with Session(engine) as session:
# 팀 데이터 생성
        dev_team = Team(team_id=1, name="개발팀")
# 멤버 데이터 생성
        jimmy = Member(member_id=1, name="김재현", team=dev_team)
# 생성한 데이터 추가 및 커밋. cascade 옵션 때문에 자동으로 jimmy도 따라간다!!!!
        session.add(dev_team)
        session.commit()

        print("\n[2] 양방향 탐색")
# Member → Team (N → 1)
        print(f"{jimmy.name}의 소속팀: {jimmy.team.name}")
# Team → Members (1 → N)
        print(f"{dev_team.name}의 멤버 목록:")
        for m in dev_team.members:
            print(f"  - {m.name}")

#=======================================================
#5. 1:1 관계 모델 (User ~ Profile)
#=======================================================
class User(orm_base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(100))
    # 1:1 관계 - uselist=False로 단일 객체를 반환해야한다.
    profile = relationship('Profile', back_populates='user', uselist=False)
    # 디버깅용 객체 문자열 출력을 위한 매직 메서드
    def __repr__(self):
        return f"<User(user_id={self.user_id}, name='{self.name}>"
class Profile(orm_base):
    __tablename__ = 'profile'
    profile_id = Column(Integer, primary_key=True)
    bio = Column(String(100))
    # 1:1 관계 - 외래키 받는 부분에 UNIQUE 옵션을 추가해야한다.
    user_id = Column(Integer, ForeignKey('users.user_id'), unique=True)
    # 1:1 관계 - 관계 매핑은 그대로.
    user= relationship('User', back_populates='profile')
    # 디버깅용 객체 문자열 출력을 위한 매직 메서드
    def __repr__(self):
        return f"<Profile(profile_id={self.profile_id}, name='{self.name}>"

#=======================================================
#6. 1:1 테스트 모듈
#=======================================================
def test_one_to_one():
    orm_base.metadata.create_all(engine)
    with Session(engine) as session:
        jimmy = User(user_id=1, email="jimmy@email.com")
        jimmy_profile = Profile(profile_id=1, bio="백엔드 개발자입니다. Python과 DB를 활용합니다.", user=jimmy)
        session.add(jimmy)
        session.commit()
        # ----- 양방향 탐색 -----
        print("\n[2] 양방향 탐색 (둘 다 단일 객체!)")
        # User → Profile
        print(f"{jimmy.email}의 프로필: {jimmy.profile.bio}")
        # Profile → User
        print(f"프로필 소유자: {jimmy_profile.user.email}")
        # ----- uselist=False 확인 -----
        print("\n[3] uselist=False 확인")
        print(f"jeff.profile 타입: {type(jimmy.profile)}")
        print("→ 리스트가 아닌 단일 Profile 객체!")

if __name__ == "__main__":
    print("기존 테이블 삭제 시작")
    orm_base.metadata.drop_all(engine)
    print("기존 테이블 삭제 완료, 생성 시작")
    orm_base.metadata.create_all(engine)
    print("새로운 테이블 생성 완료")
    #test_one_to_N()
    test_one_to_one()
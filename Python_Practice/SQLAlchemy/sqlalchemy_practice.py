from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship

#=======================================================
#1. 데이터베이스 엔진 생성
#=======================================================
engine = create_engine(
    "mysql+pymysql://kjhappy77:Fg6wL4cV9nY3kRpZ@180.69.158.131:3397/schema_kjhappy77", echo=True
)
# ======================================================
# 2. ORM_BASE Class 생성
# ======================================================
# 모든 ORM Model Class는 이 Base를 상속받습니다
orm_base = declarative_base()
#=======================================================
#3-1. Team 클래스 정의
#=======================================================
class Team(orm_base):
# schema_kjhappy77.teams 테이블에 매핑되는 클래스 생성 ===
    __tablename__ = 'teams'
# 컬럼 정의, team_id : INT(PK) / name : VARCHAR(100)
    team_id = Column(Integer, primary_key=True)
    name = Column(String(100))
# Member 클래스와 관계 설정 (relationship 활용)
# back_populates에는 '상대방 클래스의 필드명' 기입
# Member 클래스의 'team' 필드와 연결함.
    """양방향 연결 지점"""
    members = relationship('Member', back_populates='team')
# 디버깅용 객체 문자열 출력을 위한 매직 메서드
    def __repr__(self):
        return f"<Team(team_id={self.team_id}, name='{self.name}>"
#=======================================================
#3-2. Member 클래스 정의
#=======================================================
class Member(orm_base):
# schema_kjhappy77.members 테이블에 매핑되는 클래스 생성
    __tablename__ = 'members'
# 컬럼 정의, member_id : INT(PK) / name : VARCHAR(100) / team_id(FK)
    member_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    team_id = Column(Integer, ForeignKey('teams.team_id'))
# Team 클래스와 관계 설정 (relationship 활용)
# back_populates에는 '상대방 클래스의 필드명' 기입
# Member 클래스의 'members' 필드와 연결함.
    """양방향 연결 지점"""
    team = relationship('Team', back_populates='members')
# 디버깅용 객체 문자열 출력을 위한 매직 메서드
    def __repr__(self):
        return f"<Member(member_id={self.team_id}, name='{self.name}>"
# ======================================================
# 4. Create - 데이터 생성하기
# ======================================================
def create_data():
    with Session(engine) as session:
# Team 객체 생성
        dev_team = Team(team_id=10, name="개발팀")
        design_team = Team(team_id=20, name="디자인팀")
# Member 객체 생성 (team 속성으로 관계 설정)
        jimmy = Member(member_id=1, name="김재현", team=dev_team)
        chulsoo = Member(member_id=2, name="김철수", team=dev_team)
        younghee = Member(member_id=3, name="이영희", team=design_team)
# 세션에 추가. Team을 추가하면 연관된 Member 클래스도 자동으로 추가된다! "cascade"
        session.add(dev_team)
        session.add(design_team)
        session.add_all([jimmy, chulsoo, younghee])
# DB 반영 (INSERT 쿼리 실행)
        session.commit()
# 실제 오퍼레이션 종료. 로깅을 위한 출력
        print("\n=== 데이터 생성 완료 ===")
        print(f"생성된 팀 : {dev_team}, {design_team}")
        print(f"생성된 멤버 : {jimmy}, {chulsoo}, {younghee}")
# ======================================================
# 5. Read - 데이터 조회하기
# ======================================================
def read_data():
    with Session(engine) as session:
# PK 활용 조회
        print("==========PK활용============")
        member = session.get(Member, 1)
        print(f"조회된 멤버 : {member}, 이름 : {member.name}")
# 연관 객체 조회
        print("====(Member -> Team)=======")
        print(f"{member.name}의 소속팀 : {member.team.name}")
# 역방향 조회
        print("====(Team -> Member)========")
        team = session.get(Team, 10)
        print(f"{team.name}의 멤버 목록:")
        for m in team.members:
            print(f"    - {m.name}")
# ======================================================
# 6. Update - 데이터 수정하기
# ======================================================
def update_data():
    with Session(engine) as session:
# 수정 대상 멤버 조회
        member = session.get(Member, 1)
        print(f"수정 대상 멤버 : {member}")
# 속성 값만 변경
        member.name = "김재현(쿼리없이수정할수있음)"
# session.commit 시점에 자동으로 Update SQL 생성 & 커밋
        session.commit()
        print(f"수정 결과 : {member}")
# ======================================================
# 7. Delete - 데이터 삭제하기
# ======================================================
def delete_data():
    with Session(engine) as session:
# 삭제할 멤버 조회
        member = session.get(Member, 3)  # 이영희
        print(f"\n=== 삭제 대상 ===")
        print(f"멤버: {member}")
# 삭제
        session.delete(member)
# session.commit 시점에 자동으로 Update SQL 생성 & 커밋
        session.commit()
# 삭제 확인
        deleted_member = session.get(Member, 3)
        print(f"삭제된 멤버 조회 결과: {deleted_member}")

if __name__ == "__main__":
#    create_data()
#    read_data()
#    update_data()
    delete_data()
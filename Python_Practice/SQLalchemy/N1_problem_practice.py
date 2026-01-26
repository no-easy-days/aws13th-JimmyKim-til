from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, event
from sqlalchemy.orm import declarative_base, Session, relationship, joinedload

#=======================================================
#1. 데이터베이스 엔진 생성 ---- GITHUB 푸쉬 전에 수정!!
#=======================================================
engine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/orm_practice",
    echo=True  # SQL 로그 출력
)

# ======================================================
# 2. ORM_BASE Class 생성
# ======================================================
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
    member_list = relationship('Member', back_populates='belong_to_team')
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
    belong_to_team = relationship('Team', back_populates='member_list')
# 디버깅용 객체 문자열 출력을 위한 매직 메서드
    def __repr__(self):
        return f"<Member(member_id={self.team_id}, name='{self.name}>"

#=======================================================
#4. 쿼리 카운터 만들기(SELECT만 카운트)
#=======================================================
query_count = 0

@event.listens_for(engine, "before_cursor_execute")
def count_queries(conn, cursor, statement, parameters, context, executemany):
    global query_count
# SELECT 쿼리만 카운트 (테이블 생성/삽입 쿼리 제외)
    if statement.strip().upper().startswith("SELECT") and "FROM members" in statement or "FROM teams" in statement:
        query_count += 1

def reset_query_count():
    global query_count
    query_count = 0

def get_query_count():
    return query_count

#=======================================================
#5. 테이블 생성(기존 테이블 DROP 후 CREATE)
#=======================================================
def setup_tables():
    #기존 테이블 삭제, 생성
    print("기존 테이블 삭제 시작")
    orm_base.metadata.drop_all(engine)
    print("기존 테이블 삭제 완료, 생성 시작")
    orm_base.metadata.create_all(engine)
    print("새로운 테이블 생성 완료")

#=======================================================
#6. 테스트 데이터 삽입
#=======================================================
def insert_test_data():
    with Session(engine) as session:
# 팀 100개 생성. 멤버와 1:1매칭
        teams = []
        for i in range(1, 101):
            team = Team(team_id=i, name=f"팀{i:03d}")
            teams.append(team)
        session.add_all(teams)
# 멤버 100명 생성
        members = []
        for i in range(1, 101):
            member = Member(member_id=i, name=f"멤버{i:03d}", team_id=i)
            members.append(member)
        session.add_all(members)

        session.commit()
        print(f"팀, 멤버 각각 100명 생성 완료")

#=======================================================
#7. N+1 문제 발생 (Lazy Loading)
#=======================================================
def demonstrate_n_plus_1_problem():
# 쿼리 카운트 0으로 초기화
    reset_query_count()
# 시작
    with Session(engine) as session:
        members = session.query(Member).all()
        print(f"조회된 총 멤버 수 : {len(members)}명")
        print("멤버의 각각의 팀 이름 출력")
        for member in members:
            team_name = member.belong_to_team.name
            print(f"  {member.name}  -->  {team_name}")

        print(f"실행된 쿼리 수 : {get_query_count()}개")

# =======================================================
# 7. N+1 문제 발생 (Lazy Loading)
# =======================================================
def demonstrate_n_plus_1_problem():
    # 쿼리 카운트 0으로 초기화
    reset_query_count()
    # 시작
    with Session(engine) as session:
        members = session.query(Member).all()
        print(f"조회된 총 멤버 수 : {len(members)}명")
        print("멤버의 각각의 팀 이름 출력")
        for member in members:
            team_name = member.belong_to_team.name
            print(f"  {member.name}  -->  {team_name}")

        print(f"실행된 쿼리 수 : {get_query_count()}개")

# =======================================================
# 8. N+1 문제 해결 방식 (Eager Loading)
# =======================================================
def solve_n_plus_1_problem_with_joinedload():
    # 쿼리 카운트 0으로 초기화
    reset_query_count()
    # 시작
    with Session(engine) as session:
# 멤버와 팀을 JOIN을 활용하여 한번에 조회한다.
        members = session.query(Member).options(joinedload(Member.belong_to_team)).all()
        print(f"조회된 총 멤버 수 : {len(members)}명")
        print("멤버의 각각의 팀 이름 출력 --------- 여기 하위로는 동일함")
        for member in members:
            team_name = member.belong_to_team.name
            print(f"  {member.name}  -->  {team_name}")

        print(f"실행된 쿼리 수 : {get_query_count()}개")

if __name__ == "__main__":
    setup_tables()
    insert_test_data()
    demonstrate_n_plus_1_problem()
    solve_n_plus_1_problem_with_joinedload()

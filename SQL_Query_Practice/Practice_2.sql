-- SQLAlchemy (ORM) 실습용 SQL
-- 기존 테이블이 있다면 삭제 (실습 초기화용)
USE schema_kjhappy77;
DROP TABLE members;

DROP TABLE teams;

-- teams 테이블 생성
CREATE TABLE teams(
	team_id INT PRIMARY KEY,
    name VARCHAR(100)
    );

-- members 테이블 생성
CREATE TABLE members(
	member_id INT PRIMARY KEY,
	name VARCHAR(100),
	team_id INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
    );
    
-- 테이블 확인
SHOW Tables;
SHOW CREATE TABLE members;
DESCRIBE members;
DESCRIBE teams;

SELECT*FROM teams;
SELECT*FROM members;
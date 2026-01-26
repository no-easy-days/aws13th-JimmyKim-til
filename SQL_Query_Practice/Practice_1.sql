-- 최초 연결 테스트 -- 
/*
쿼리에서 SQL 키워드는 대문자, 테이블명과 컬럼은 소문자로 쓰는 것이 관례
*/

SHOW TABLES IN demo;
SELECT*FROM demo.users;

-- 문제 4. SQL 실습. users 테이블의 구조(컬럼 정보) 확인 --
DESCRIBE demo.users;
SELECT name FROM demo.users;

-- MariaDB 접속 환경 설정 --
SELECT now();
SHOW DATABASES; ## --- 데이터베이스 목록 확인

-- 작업할 데이터베이스 선택 및 확인 --
USE schema_kjhappy77;
SELECT DATABASE();
SHOW TABLES;

-- users 테이블 새로 생성하기 --
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, email VARCHAR(100), age INT);
SHOW TABLES;
DESCRIBE schema_kjhappy77.users;

-- 실습 1. 게시글 테이블 만들기 --
CREATE TABLE posts (id INT auto_increment primary key, title VARCHAR(200) NOT NULL, content TEXT, created_at DATETIME);

-- 실습 2. 상품 테이블 만들기 --
CREATE TABLE products (id INT auto_increment primary key, name VARCHAR(100) NOT NULL, price INT NOT NULL, stock INT, is_available BOOLEAN);

-- 실습 3. 회원 테이블 만들기 --
CREATE TABLE members (user_id INT auto_increment primary key, user_name VARCHAR(50) NOT NULL, email_address VARCHAR(100), phone_number VARCHAR(20), registered_date date, user_points int);

-- 실습 4. 테이블 확인하기 --
SHOW Tables;
Describe posts;
Describe products;
DESCRIBE members;
DESCRIBE orders;

-- 실습문제 INSERT --
INSERT INTO products (name, price, stock ) VALUES ('무선 키보드', 45000, 100);
INSERT INTO users (name, email, age) VALUES ('철수', 'cheolsu@example.com', 25), ('영희', 'younghee@example.com', 23), ('훈이', 'hooni@example.com', 24);
INSERT INTO users (name) VALUES('짱구');
INSERT INTO users (name) VALUES('O''Brien');

INSERT INTO orders (user_id, product_name, quantity, order_date) VALUES
    (1, '무선 키보드', 2, '2026-01-15'),
    (1, '무선 마우스', 1, '2026-01-15'),
    (2, '모니터', 1, '2026-01-16'),
    (3, 'USB 허브', 3, NULL),           -- order_date 미정
    (2, '노트북 거치대', 1, '2026-01-18')
    ;
    
-- 실습문제 SELECT -- 
INSERT INTO users (name, email, age) VALUES 
('철수', 'cs@example.com', 25),
('영희', 'yh@example.com', 23),
('훈이', 'hi@example.com', 27),
('짱구', NULL, 22),
('jeff', 'jeff@example.com', 30);

DROP TABLE users;

SELECT name, age FROM users;
SELECT*FROM users WHERE age >= 25;
SELECT name, age FROM users WHERE age >= 20 AND age <=25;
SELECT*FROM users WHERE name = '철수' OR age = 30;
SELECT*FROM users WHERE email is NULL;
SELECT*FROM users WHERE email LIKE '%example%';
SELECT*FROM users WHERE name LIKE '영%';

SELECT name, email FROM users WHERE email is NULL AND age <= 25;
SELECT*FROM users WHERE name LIKE '__';

-- 실습문제 UPDATE --
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price INT NOT NULL,
    stock INT DEFAULT 0,
    category VARCHAR(50)
);

INSERT INTO products (name, price, stock, category) VALUES
('노트북', 1200000, 10, '전자기기'),
('마우스', 25000, 50, '전자기기'),
('키보드', 80000, 30, '전자기기'),
('책상', 150000, 5, '가구'),
('의자', 200000, 8, '가구');

SELECT * FROM products;

SELECT price FROM products WHERE id = 1;
UPDATE products SET price = 1100000 WHERE id = 1;

SELECT price, stock FROM products WHERE id = 2;
UPDATE products SET price = 30000, stock = 45 WHERE id = 2;

UPDATE products SET price = price * 1.1 WHERE category = '전자기기'; -- mysql 에러 발생함. safe update mode 비활성화 필요.
SELECT price FROM products;

UPDATE products SET stock = 20 WHERE stock <= 10;
UPDATE products SET category = NULL WHERE id = 5 ;

UPDATE products SET price = price - 50000 WHERE category = '가구';

SELECT price FROM products WHERE price >= 100000;
UPDATE products SET price = price * 0.95 WHERE price >= 100000;
SELECT category FROM products WHERE stock = 0;
UPDATE products SET category = '품절' WHERE stock = 0;
SELECT stock FROM products WHERE category = '전자기기';
UPDATE products SET stock = stock + 5 WHERE category = '전자기기';

-- JOIN 연습해보기 쿼리 --
USE schema_kjhappy77;
SELECT * FROM users;
SELECT u.name, p.title FROM schema_kjhappy77.users u INNER JOIN schema_kjhappy77.posts p ON u.id = p.user_id;

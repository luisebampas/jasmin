#CREATE TABLE items (
#	itemnum INT,
#	catenum INT,
#	authornum INT,
#	itemname NVARCHAR(40),
#	price INT,
#	itemdate DATE,
#	iteminfo NVARCHAR(200),
#	downloads INT,
#	series INT
#);
ALTER TABLE items AUTO_INCREMENT = 1;

# items data
SET @tseries = 101;
INSERT INTO items VALUES (101, 2, 1, '테스트용1-1', 8000, '2020-02-05', '테스트용1-1권', 999, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용1-2', 8000, '2020-02-06', '테스트용1-2권', 899, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용1-3', 8000, '2020-02-07', '테스트용1-3권', 799, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용1-4', 8000, '2020-02-07', '테스트용1-4권', 699, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용1-5', 8000, '2020-02-08', '테스트용1-5권', 599, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용1-6', 8000, '2020-02-08', '테스트용1-6권', 499, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용1-7', 8000, '2020-02-08', '테스트용1-7권', 399, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용1-8', 8000, '2020-02-08', '테스트용1-8권', 299, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용1-9', 8000, '2020-02-09', '테스트용1-9권', 199, @tseries);

SET @tseries = (SELECT LAST_INSERT_ID() + 1);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용2-1', 9000, '2020-02-10', '테스트용2-1권', 999, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용2-2', 9000, '2020-02-11', '테스트용2-2권', 989, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용2-3', 9000, '2020-02-12', '테스트용2-3권', 979, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용2-4', 9000, '2020-02-13', '테스트용2-4권', 969, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용2-5', 9000, '2020-02-14', '테스트용2-5권', 959, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용2-6', 9000, '2020-02-15', '테스트용2-6권', 949, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용2-7', 9000, '2020-02-16', '테스트용2-7권', 939, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용2-8', 9000, '2020-02-17', '테스트용2-8권', 929, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용2-9', 9000, '2020-02-18', '테스트용2-9권', 919, @tseries);

SET @tseries = (SELECT LAST_INSERT_ID() + 1);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용3-1', 10000, '2020-02-18', '테스트용3-1권', 999, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용3-2', 10000, '2020-02-18', '테스트용3-2권', 998, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용3-3', 10000, '2020-02-18', '테스트용3-3권', 997, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용3-4', 10000, '2020-02-18', '테스트용3-4권', 996, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용3-5', 10000, '2020-02-18', '테스트용3-5권', 995, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용3-6', 10000, '2020-02-18', '테스트용3-6권', 994, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용3-7', 10000, '2020-02-18', '테스트용3-7권', 993, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용3-8', 10000, '2020-02-18', '테스트용3-8권', 992, @tseries);
INSERT INTO items VALUES (itemnum, 2, 1, '테스트용3-9', 10000, '2020-02-18', '테스트용3-9권', 991, @tseries);

SET @tseries = (SELECT LAST_INSERT_ID() + 1);
INSERT INTO items VALUES (itemnum, 2, 2, '가 테스트용4-1', 7000, '2020-02-19', '테스트용4-1권', 989, @tseries);
INSERT INTO items VALUES (itemnum, 2, 2, '가 테스트용4-2', 7000, '2020-02-20', '테스트용4-2권', 988, @tseries);
INSERT INTO items VALUES (itemnum, 2, 2, '가 테스트용4-3', 7000, '2020-02-21', '테스트용4-3권', 987, @tseries);
INSERT INTO items VALUES (itemnum, 2, 2, '가 테스트용4-4', 7000, '2020-02-22', '테스트용4-4권', 986, @tseries);
INSERT INTO items VALUES (itemnum, 2, 2, '가 테스트용4-5', 7000, '2020-02-23', '테스트용4-5권', 985, @tseries);
INSERT INTO items VALUES (itemnum, 2, 2, '가 테스트용4-6', 7000, '2020-02-24', '테스트용4-6권', 984, @tseries);
INSERT INTO items VALUES (itemnum, 2, 2, '가 테스트용4-7', 7000, '2020-02-25', '테스트용4-7권', 983, @tseries);
INSERT INTO items VALUES (itemnum, 2, 2, '가 테스트용4-8', 7000, '2020-02-26', '테스트용4-8권', 982, @tseries);
INSERT INTO items VALUES (itemnum, 2, 2, '가 테스트용4-9', 7000, '2020-02-27', '테스트용4-9권', 981, @tseries);

SET @tseries = (SELECT LAST_INSERT_ID() + 1);
INSERT INTO items VALUES (itemnum, 12, 2, '다 테스트용5-1', 7000, '2020-03-01', '테스트용5-1권', 989, @tseries);
INSERT INTO items VALUES (itemnum, 12, 2, '다 테스트용5-2', 7000, '2020-03-02', '테스트용5-2권', 988, @tseries);

SET @tseries = (SELECT LAST_INSERT_ID() + 1);
INSERT INTO items VALUES (itemnum, 12, 3, '나 테스트용6', 7000, '2020-03-01', '테스트용6 정보', 99, @tseries);

SET @tseries = (SELECT LAST_INSERT_ID() + 1);
INSERT INTO items VALUES (itemnum, 12, 3, '바 테스트용7', 7000, '2020-03-01', '테스트용7 정보', 99, @tseries);

SET @tseries = (SELECT LAST_INSERT_ID() + 1);
INSERT INTO items VALUES (itemnum, 2, 3, '라 테스트용8', 7000, '2020-03-01', '테스트용8-1권', 99, @tseries);
INSERT INTO items VALUES (itemnum, 2, 3, '라 테스트용8', 7000, '2020-03-01', '테스트용8-2권', 99, @tseries);
INSERT INTO items VALUES (itemnum, 2, 3, '라 테스트용8', 7000, '2020-03-01', '테스트용8-3권', 99, @tseries);

INSERT INTO items VALUES (1000, 1, 1000, '테스트용', 100000, CURRENT_DATE(), '테스트용책입니다.', 1000, 1000);
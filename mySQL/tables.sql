DROP DATABASE teamp;
CREATE DATABASE teamp;
USE teamp;

# 기본 테이블 
CREATE TABLE authors (
	authornum INT,
	authorname NVARCHAR(20),
	authorinfo NVARCHAR(50)
);

CREATE TABLE formats (
	formatnum INT,
	formatname VARCHAR(20)
);

CREATE TABLE levelofcate (
	catelevel INT,
	levelname NVARCHAR(10)
);

CREATE TABLE category (
	catenum INT,
	catelevel INT,
	catename NVARCHAR(10),
	pcatenum INT
);

CREATE TABLE items (
	itemnum INT,
	catenum INT,
	authornum INT,
	formatnum INT,
	itemname NVARCHAR(20),
	price INT,
	itemimg VARCHAR(50),
	itemdate DATE,
	downloads INT
);

CREATE TABLE users (
	usernum INT,
	userid VARCHAR(20),
	userpwd VARCHAR(20),
	username VARCHAR(20)
);

CREATE TABLE carts (
	usernum INT,
	itemnum INT
);

CREATE TABLE orders (
	ordernum INT,
	usernum INT,
	totalprice INT,
	ordersummary VARCHAR(50)
);

CREATE TABLE orderlist (
	ordernum INT,
	usernum INT,
	itemnum INT
);

CREATE TABLE payment (
	ordernum INT,
	usernum INT,
	paydate DATETIME,
	cost INT
);

# 추가 테이블 
# 쿠폰 
CREATE TABLE coupons (
	couponnum INT,
	catenum INT
);

CREATE TABLE couponlist (
	couponpin INT,
	couponnum INT,
	usernum INT,
	discount INT,
	issuedate DATE,
	expdate DATE,
	useddate DATE
);

CREATE TABLE couponused (
	ordernum INT,
	usernum INT,
	couponpin INT
);

# 관심분야 
CREATE TABLE interests (
	usernum INT,
	catenum INT
);

########################################authors
# 제약조건 
# primary key
ALTER TABLE authors ADD CONSTRAINT authornum_pk PRIMARY KEY (authornum);
ALTER TABLE formats ADD CONSTRAINT formatnum_pk PRIMARY KEY (formatnum);
ALTER TABLE levelofcate ADD CONSTRAINT catelevel_pk PRIMARY KEY (catelevel);
ALTER TABLE category ADD CONSTRAINT catenum_pk PRIMARY KEY (catenum);
ALTER TABLE items ADD CONSTRAINT itemnum_pk PRIMARY KEY (itemnum);
ALTER TABLE users ADD CONSTRAINT usernum_pk  PRIMARY KEY (usernum);
ALTER TABLE orders ADD CONSTRAINT ordernum_pk PRIMARY KEY (ordernum);

# auto increment
ALTER TABLE authors MODIFY authornum INT NOT NULL AUTO_INCREMENT;
ALTER TABLE authors AUTO_INCREMENT = 1001;
ALTER TABLE items MODIFY itemnum INT NOT NULL AUTO_INCREMENT;
ALTER TABLE items AUTO_INCREMENT = 10001;
ALTER TABLE users MODIFY usernum INT NOT NULL AUTO_INCREMENT;
ALTER TABLE users AUTO_INCREMENT = 100001;
ALTER TABLE orders MODIFY ordernum INT NOT NULL AUTO_INCREMENT;
ALTER TABLE orders AUTO_INCREMENT = 1000001;

# foreign key
ALTER TABLE category ADD CONSTRAINT category_catelevel FOREIGN KEY (catelevel) REFERENCES levelofcate(catelevel);
ALTER TABLE items ADD CONSTRAINT items_catenum FOREIGN KEY (catenum) REFERENCES category(catenum);
ALTER TABLE items ADD CONSTRAINT items_authornum FOREIGN KEY (authornum) REFERENCES authors(authornum);
ALTER TABLE items ADD CONSTRAINT items_formatnum FOREIGN KEY (formatnum) REFERENCES formats(formatnum);
ALTER TABLE carts ADD CONSTRAINT carts_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);
ALTER TABLE carts ADD CONSTRAINT carts_itemnum FOREIGN KEY (itemnum) REFERENCES items(itemnum);
ALTER TABLE orderlist ADD CONSTRAINT orderlist_ordernum FOREIGN KEY (ordernum) REFERENCES orders(ordernum);
ALTER TABLE orderlist ADD CONSTRAINT orderlist_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);
ALTER TABLE orderlist ADD CONSTRAINT orderlist_itemnum FOREIGN KEY (itemnum) REFERENCES items(itemnum);
ALTER TABLE payment ADD CONSTRAINT payment_ordernum FOREIGN KEY (ordernum) REFERENCES orders(ordernum);
ALTER TABLE payment ADD CONSTRAINT payment_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);

DROP DATABASE jasminDb;
CREATE DATABASE jasminDb;
USE jasminDb;

# 기본 테이블 
CREATE TABLE authors (
	authornum INT,
	authorname NVARCHAR(20) NOT NULL,
	authorinfo NVARCHAR(1000)
);

CREATE TABLE category (
	catenum INT,
	catename NVARCHAR(10) NOT NULL
);

CREATE TABLE items (
	itemnum INT,
	catenum INT NOT NULL,
	authornum INT NOT NULL,
	itemname NVARCHAR(40) NOT NULL,
	price INT NOT NULL,
	itemdate DATE NOT NULL,
	iteminfo NVARCHAR(1000),
	sells INT NOT NULL,
	series INT NOT NULL
);

CREATE TABLE users (
	usernum INT,
	userid VARCHAR(20),
	userpwd VARCHAR(20) NOT NULL,
	username VARCHAR(20) NOT NULL
);

CREATE TABLE carts (
	usernum INT,
	itemnum INT
);

CREATE TABLE orders (
	ordernum INT,
	usernum INT,
	totalprice INT,
	ordersummary VARCHAR(100)
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
# 리뷰
CREATE TABLE comments (
	itemnum INT,
	usernum INT,
	eval INT,
	cmt NVARCHAR(200)
);

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
	canuse BOOL
);

CREATE TABLE couponused (
	couponpin INT,
	usernum INT,
	ordernum INT
);

# 관심분야 
CREATE TABLE interests (
	usernum INT,
	catenum INT
);

########################################authors
# 제약조건 
# primary key, unique
ALTER TABLE authors ADD CONSTRAINT authors_pk PRIMARY KEY (authornum);
ALTER TABLE category ADD CONSTRAINT category_pk PRIMARY KEY (catenum);
ALTER TABLE items ADD CONSTRAINT items_pk PRIMARY KEY (itemnum);
ALTER TABLE users ADD CONSTRAINT users_pk  PRIMARY KEY (usernum);
ALTER TABLE users ADD CONSTRAINT users_id_unique UNIQUE (userid);
ALTER TABLE orders ADD CONSTRAINT orders_pk PRIMARY KEY (ordernum);
ALTER TABLE coupons ADD CONSTRAINT coupons_pk PRIMARY KEY (couponnum);
ALTER TABLE couponlist ADD CONSTRAINT couponlist_pk PRIMARY KEY (couponpin);

# auto increment
ALTER TABLE authors MODIFY authornum INT NOT NULL AUTO_INCREMENT;
ALTER TABLE items MODIFY itemnum INT NOT NULL AUTO_INCREMENT;
ALTER TABLE users MODIFY usernum INT NOT NULL AUTO_INCREMENT;
ALTER TABLE orders MODIFY ordernum INT NOT NULL AUTO_INCREMENT;
ALTER TABLE coupons MODIFY couponnum INT NOT NULL AUTO_INCREMENT;
ALTER TABLE couponlist MODIFY couponpin INT NOT NULL AUTO_INCREMENT;

# foreign key
ALTER TABLE items ADD CONSTRAINT items_catenum FOREIGN KEY (catenum) REFERENCES category(catenum);
ALTER TABLE items ADD CONSTRAINT items_authornum FOREIGN KEY (authornum) REFERENCES authors(authornum);
ALTER TABLE carts ADD CONSTRAINT carts_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);
ALTER TABLE carts ADD CONSTRAINT carts_itemnum FOREIGN KEY (itemnum) REFERENCES items(itemnum);
ALTER TABLE orderlist ADD CONSTRAINT orderlist_ordernum FOREIGN KEY (ordernum) REFERENCES orders(ordernum);
ALTER TABLE orderlist ADD CONSTRAINT orderlist_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);
ALTER TABLE orderlist ADD CONSTRAINT orderlist_itemnum FOREIGN KEY (itemnum) REFERENCES items(itemnum);
ALTER TABLE payment ADD CONSTRAINT payment_ordernum FOREIGN KEY (ordernum) REFERENCES orders(ordernum);
ALTER TABLE payment ADD CONSTRAINT payment_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);
ALTER TABLE comments ADD CONSTRAINT comments_itemnum FOREIGN KEY (itemnum) REFERENCES items(itemnum);
ALTER TABLE comments ADD CONSTRAINT comments_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);
ALTER TABLE coupons ADD CONSTRAINT coupons_catenum FOREIGN KEY (catenum) REFERENCES category(catenum);
ALTER TABLE couponlist ADD CONSTRAINT couponlist_couponnum FOREIGN KEY (couponnum) REFERENCES coupons(couponnum);
ALTER TABLE couponlist ADD CONSTRAINT couponlist_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);
ALTER TABLE couponused ADD CONSTRAINT couponused_couponpin FOREIGN KEY (couponpin) REFERENCES couponlist(couponpin);
ALTER TABLE couponused ADD CONSTRAINT couponused_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);
ALTER TABLE couponused ADD CONSTRAINT couponused_ordernum FOREIGN KEY (ordernum) REFERENCES orders(ordernum);
ALTER TABLE interests ADD CONSTRAINT interests_usernum FOREIGN KEY (usernum) REFERENCES users(usernum);
ALTER TABLE interests ADD CONSTRAINT interests_catenum FOREIGN KEY (catenum) REFERENCES category(catenum);

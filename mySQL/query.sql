# paging
# offset에는 20 * (페이지번호- 1)
##########
# 검색조건 
## 카테고리 
# WHERE catenum = 2 
## 검색어 
# AND CONCAT (itemname, a.authorname) LIKE '%{{검색어}}%'
# AND itemname LIKE '%{{검색어}}%'
# AND a.authorname LIKE '%{{검색어}}%'
##########
## 정렬조건 
## 번호순(최신등록순) 
# ORDER BY itemnum DESC
## 출간일순(최신순) 
# ORDER BY itemdate ASC 
## 누적판매량순 
# ORDER BY download DESC
## 상품명순(오름차순 - 내림차순시 DESC) 
# ORDER BY itemname ASC
## 가격순(오름차순 - 내림차순시 DESC) 
# ORDER BY price ASC
##########
SELECT i.itemnum, i.itemname, a.authorname, i.price, i.itemdate 
FROM items i LEFT OUTER JOIN authors a 
ON i.authornum = a.authornum 
# 검색조건 
WHERE catenum IS NOT NULL 
AND CONCAT (itemname, a.authorname) LIKE '%%'
# 정렬조건 
ORDER BY itemnum DESC 
LIMIT 20 OFFSET 0;

# count list
SELECT COUNT(itemnum) 
FROM items i LEFT OUTER JOIN authors a 
ON i.authornum = a.authornum 
WHERE catenum IS NOT NULL;

# test itemnum
SET @test_itemnum = 128;

# item detail
SELECT i.itemnum, i.catenum, i.itemname, i.price, i.itemdate, i.iteminfo, i.sells, i.series, a.authorname, a.authorinfo 
FROM items i LEFT OUTER JOIN authors a 
ON i.authornum = a.authornum 
WHERE itemnum = @test_itemnum;

# series list
SELECT itemnum, itemname, price FROM items
WHERE series = (SELECT series FROM items WHERE itemnum = @test_itemnum);

# search author
SELECT authorname, authornum FROM authors 
WHERE authorname LIKE '%윤재우%'
ORDER BY authornum ASC;

# recent published books
SELECT itemname, itemdate, price FROM items
WHERE authornum = 1
ORDER BY itemdate DESC
LIMIT 10;

# get auto_increment of items table
SELECT AUTO_INCREMENT FROM information_schema.tables WHERE table_name = 'items' AND table_schema = DATABASE();
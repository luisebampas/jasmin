# paging
# offset에는 20 * (페이지번호- 1)
##########
## 검색조건 
# WHERE itemname LIKE '%{{검색어}}%'
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
WHERE itemname LIKE '%%'
# 정렬조건 
ORDER BY itemnum DESC
LIMIT 20 OFFSET 0;

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

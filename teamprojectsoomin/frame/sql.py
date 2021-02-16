class Sql:

    # 1. 회원 개인정보 #
    userlist = 'SELECT * FROM users';
    userlistone = "SELECT * FROM users WHERE userid='%s'";
    userinsert = "INSERT INTO users VALUES (null,'%s','%s','%s')";
    userdelete = "DELETE FROM users WHERE userid= '%s'";
    userupdate = "UPDATE users SET userpwd='%s', username='%s' WHERE userid='%s'";

    # 2. 유저의 주문이력 정보 #
    orderlistone = "SELECT * FROM orderlist WHERE usernum=%d ORDER BY ordernum DESC LIMIT 1";
    orderlistinsert = "INSERT INTO orderlist VALUES (%d,%d,%d)";


    # 4. 사용자의 장바구니 정보 #
    main = "SELECT o.ordernum, i.itemnum, i.itemname, i.price, a.authorname FROM orderlist o INNER JOIN items i ON o.itemnum = i.itemnum INNER JOIN authors a ON i.authornum = a.authornum where o.usernum = %d"
    cart = "SELECT c.cartnum, c.itemnum, i.itemname, i.price FROM carts c INNER JOIN items i ON c.itemnum = i.itemnum where c.usernum = %d "
    cartinsert = "INSERT INTO carts VALUES (null,%d,%d)";
    cartdelete = "DELETE FROM carts WHERE cartnum= %d ";



    # 5. 총 결제 정보
    paymentinsert = "INSERT INTO payment VALUES (%d,%d,'%s',CURRENT_DATE,%d)";
    paymentselect = "SELECT * FROM payment";
    paymentselectone = "SELECT * FROM payment WHERE usernum=%d ORDER BY ordernum DESC";



    # 6. 관리자의 총 주문/판매 정보 #
    ordersinsert = "INSERT INTO orders VALUES (null,%d,%d,'%s')";
    ordersselect = "SELECT * FROM orders";
    odersselectone = "SELECT ordernum FROM orders WHERE usernum=%d ORDER BY ordernum DESC LIMIT 1"; # ordernum만 추출.


    # 관리자의 보유상품 정보 #
    itemlist = """SELECT i.itemnum, i.itemname, a.authorname, i.price, i.itemdate, i.sells 
                  FROM items i LEFT OUTER JOIN authors a 
                  ON i.authornum = a.authornum """;
    categoryAll = "WHERE catenum IS NOT NULL ";
    category = "WHERE catenum = %d ";

    searchAll = "AND CONCAT (itemname, a.authorname) LIKE '%"
    searchWithTitle = "AND itemname LIKE '%"
    searchWithAuthor = "AND a.authorname LIKE '%"
    ordercon1 = "ORDER BY itemnum DESC ";
    ordercon2 = "ORDER BY itemdate DESC ";
    ordercon3 = "ORDER BY sells DESC ";
    ordercon4 = "ORDER BY itemname ASC ";
    ordercon5 = "ORDER BY itemname DESC ";
    ordercon6 = "ORDER BY price ASC ";
    ordercon7 = "ORDER BY price DESC ";
    page = " LIMIT %d OFFSET %d";
    itemlistcount = """SELECT COUNT(itemnum) FROM items i LEFT OUTER JOIN authors a ON i.authornum = a.authornum """;
    itemlistone = """SELECT i.itemnum, i.catenum, i.itemname, i.price, i.itemdate, i.iteminfo, i.sells, i.series, a.authorname, a.authorinfo 
                     FROM items i LEFT OUTER JOIN authors a ON i.authornum = a.authornum 
                     WHERE itemnum = %d""";
    iteminsert = """INSERT INTO items (catenum, authornum, itemname, price, itemdate, iteminfo, sells, series)
                    VALUES (%d, %d, '%s', %d, '%s', '%s', %d, %d)""";
    itemautoincre = "SELECT AUTO_INCREMENT FROM information_schema.tables WHERE table_name = 'items' AND table_schema = DATABASE()";
    itemdelete = "DELETE FROM items WHERE itemnum=%d";
    itemupdate = "UPDATE items SET catenum=%d, authornum=%d, itemname='%s', price=%d, itemdate='%s', iteminfo='%s', series=%d WHERE itemnum=%d";

    recentPublished = "SELECT itemnum, catenum, itemname, itemdate, price, series FROM items WHERE authornum = %d ORDER BY itemnum DESC LIMIT %d"
    searchAuthorNameFront = "SELECT authorname, authornum FROM authors WHERE authorname LIKE '%"
    searchAuthorNameRear = "%' ORDER BY authornum ASC"
    authorinsert = "INSERT INTO authors VALUES (NULL, '%s', '%s')";

    sellitem = "UPDATE items SET sells=sells+1 WHERE itemnum=%d"; # 결제후 해당 상품의 판매량 +1


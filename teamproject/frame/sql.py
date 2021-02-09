class Sql:
    userlist = 'SELECT * FROM users';
    userlistone = "SELECT * FROM users WHERE userid='%s'";
    userinsert = "INSERT INTO users VALUES (null,'%s','%s','%s')";
    userdelete = "DELETE FROM users WHERE userid= '%s'";
    userupdate = "UPDATE users SET userpwd='%s', username='%s' WHERE userid='%s'";
    orderlistone = "SELECT * FROM orderlist WHERE usernum=%d"
    main = "SELECT o.ordernum, i.itemnum, i.itemname, i.price, a.authorname FROM orderlist o INNER JOIN items i ON o.itemnum = i.itemnum INNER JOIN authors a ON i.authornum = a.authornum where o.usernum = %d"
    cart = "SELECT c.itemnum, i.itemname, i.price FROM carts c INNER JOIN items i ON c.itemnum = i.itemnum where c.usernum = %d "

    itemlist = """SELECT i.itemnum, i.itemname, a.authorname, i.price, i.itemdate FROM items i LEFT OUTER JOIN authors a ON i.authornum = a.authornum
                  ORDER BY itemnum DESC
               """;
    catenum = " WHERE catenum = %d"
    page = " LIMIT 20 OFFSET %d"
    itemlistone = """SELECT i.itemnum, i.catenum, i.itemname, i.price, i.itemdate, i.iteminfo, i.sells, i.series, a.authorname, a.authorinfo 
                     FROM items i LEFT OUTER JOIN authors a ON i.authornum = a.authornum 
                     WHERE itemnum = %d""";
    iteminsert = """INSERT INTO items (catenum, authornum, itemname, price, itemdate, iteminfo, downloads, series)
                    VALUES (%d, %d, '%s', %d, '%s', '%s', %d, %d)""";
    itemdelete = "DELETE FROM items WHERE itemnum=%d";
    itemupdate = "UPDATE items SET catenum=%d, authornum=%d, itemname='%s', price=%d, itemdate='%s', iteminfo='%s', series=%d WHERE itemnum=%d";

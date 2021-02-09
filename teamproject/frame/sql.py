class Sql:
    userlist = "SELECT * FROM users";
    userlistone = "SELECT * FROM users WHERE usernum=%d";
    userinsert = "INSERT INTO users (userid, userpwd, username) VALUES ('%s','%s','%s')";
    userdeletewithnum = "DELETE FROM users WHERE usernum=%d";
    userdeletewithid = "DELETE FROM users WHERE userid='%s'";
    userupdatewithnum = "UPDATE users SET pwd='%s', name='%s' WHERE usernum=%d";
    userupdatewithid = "UPDATE users SET pwd='%s', name='%s' WHERE userid='%s'";

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



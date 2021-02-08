class Sql:
    userlist = "SELECT * FROM users";
    userlistone = "SELECT * FROM users WHERE usernum=%d";
    userinsert = "INSERT INTO users (userid, userpwd, username) VALUES ('%s','%s','%s')";
    userdeletewithnum = "DELETE FROM users WHERE usernum=%d";
    userdeletewithid = "DELETE FROM users WHERE userid='%s'";
    userupdatewithnum = "UPDATE users SET pwd='%s', name='%s' WHERE usernum=%d";
    userupdatewithid = "UPDATE users SET pwd='%s', name='%s' WHERE userid='%s'";

    itemlist = "SELECT * FROM items";
    itemlistone = "SELECT * FROM items WHERE itemnum=%d";
    iteminsert = """INSERT INTO items (catenum, authornum, itemname, price, itemdate, iteminfo, downloads, series)
                    VALUES (%d, %d, '%s', %d, '%s', '%s', %d, %d)""";
    itemdelete = "DELETE FROM items WHERE itemnum=%d";
    itemupdate = "UPDATE items SET catenum=%d, authornum=%d, itemname='%s', price=%d, itemdate='%s', iteminfo='%s', series=%d WHERE itemnum=%d";



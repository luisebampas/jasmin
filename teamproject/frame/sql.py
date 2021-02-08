class Sql:
<<<<<<< HEAD
    userlist = 'SELECT * FROM users';
    userlistone = "SELECT * FROM users WHERE userid='%s'";
    userinsert = "INSERT INTO users VALUES (null,'%s','%s','%s')";
    userdelete = "DELETE FROM users WHERE userid= '%s'";
    userupdate = "UPDATE users SET userpwd='%s', username='%s' WHERE userid='%s'";

    # itemlist = "SELECT * FROM itemtb";
    # itemlistone = "SELECT * FROM itemtb WHERE id= %d ";
    # iteminsert = "INSERT INTO itemtb VALUES (null,'%s',%d,CURRENT_DATE(), '%s')";
    # itemdelete = "DELETE FROM itemtb WHERE id= %d ";
    # itemupdate = "UPDATE itemtb SET name='%s',price=%d, imgname='%s' WHERE id= %d ";
=======
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

>>>>>>> aad851d185dadcdc087b7f21a795bba5c1a79d51


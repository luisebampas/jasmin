class Sql:
    userlist = 'SELECT * FROM users';
    userlistone = "SELECT * FROM users WHERE userid='%s'";
    orderlistone = "SELECT * FROM orderlist WHERE usernum=%d"
    userinsert = "INSERT INTO users VALUES (null,'%s','%s','%s')";
    userdelete = "DELETE FROM users WHERE userid= '%s'";
    userupdate = "UPDATE users SET userpwd='%s', username='%s' WHERE userid='%s'";

    # itemlist = "SELECT * FROM itemtb";
    # itemlistone = "SELECT * FROM itemtb WHERE id= %d ";
    # iteminsert = "INSERT INTO itemtb VALUES (null,'%s',%d,CURRENT_DATE(), '%s')";
    # itemdelete = "DELETE FROM itemtb WHERE id= %d ";
    # itemupdate = "UPDATE itemtb SET name='%s',price=%d, imgname='%s' WHERE id= %d ";


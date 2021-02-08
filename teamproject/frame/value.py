class User:
    def __init__(self, usernum, userid, userpwd, username):
        self.usernum = usernum;
        self.userid = userid;
        self.userpwd = userpwd;
        self.username = username;

    def __str__(self):
        return str(self.usernum)+' '+self.userid+' '+self.userpwd+' '+self.username+' ';

class Orderlist:
    def __init__(self,  ordernum, usernum, itemnum ):
        self.ordernum = ordernum;
        self.usernum = usernum;
        self.itemnum = itemnum;

<<<<<<< HEAD
class Item:
    def __init__(self, itemnum, catenum, authornum, itemname, price, itemdate, iteminfo, sells, series):
        self.itemnum = itemnum;
        self.catenum = catenum;
        self.authornum = authornum;
        self.itemname = itemname;
        self.price = price;
        self.itemdate = itemdate;
        self.iteminfo = iteminfo;
        self.sells = sells;
        self.series = series;

    def __str__(self):
        return str(self.itemnum) + ' ' + str(self.catenum) + ' ' + str(self.authornum) + ' ' + \
               self.itemname + ' ' + str(self.price) + ' ' + str(self.itemdate) + ' ' + \
               self.iteminfo + ' ' + str(self.sells) + ' ' + str(self.series);


class Itemlist:
    def __init__(self, itemnum, itemname, authorname, price, itemdate):
        self.itemnum = itemnum;
        self.itemname = itemname;
        self.authorname = authorname;
        self.price = price;
        self.itemdate = itemdate;
=======
    def __str__(self):
        return str(self.ordernum)+' '+str(self.usernum)+' '+str(self.itemnum)+' ';
>>>>>>> master

class Mainlist:
    def __init__(self, ordernum, itemnum, itemname, price, authorname ):
        self.ordernum = ordernum;
        self.itemnum = itemnum;
        self.itemname = itemname;
        self.price = price;
        self.authorname = authorname;
    def __str__(self):
<<<<<<< HEAD
        return str(self.itemnum) + ' ' + self.itemname + ' ' + self.authorname + ' ' + \
               str(self.price) + ' ' + str(self.itemdate);
=======
        return str(self.ordernum)+' '+str(self.itemnum)+' '+self.itemname+' '+str(self.price)+' '+self.authorname+' ';

>>>>>>> master

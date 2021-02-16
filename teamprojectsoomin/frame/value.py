

class User:
    def __init__(self, usernum, userid, userpwd, username):
        self.usernum = usernum;
        self.userid = userid;
        self.userpwd = userpwd;
        self.username = username;

    def __str__(self):
        return str(self.usernum)+' '+self.userid+' '+self.userpwd+' '+self.username+' ';

class Orderlist:
    def __init__(self,  ordernum, usernum, itemnum):
        self.ordernum = ordernum;
        self.usernum = usernum;
        self.itemnum = itemnum;

    def __str__(self):
        return str(self.ordernum)+' '+str(self.usernum)+' '+str(self.itemnum)+' ';


class Mainlist:
    def __init__(self, ordernum, itemnum, itemname, price, authorname ):
        self.ordernum = ordernum;
        self.itemnum = itemnum;
        self.itemname = itemname;
        self.price = price;
        self.authorname = authorname;
    def __str__(self):
        return str(self.ordernum)+' '+str(self.itemnum)+' '+self.itemname+' '+str(self.price)+' '+self.authorname+' ';


class Cartlist:
    def __init__(self,cartnum, itemnum, itemname, price):
        self.cartnum = cartnum;
        self.itemnum = itemnum;
        self.itemname = itemname;
        self.price = price;
    def __str__(self):
        return str(self.cartnum)+' '+str(self.itemnum)+' '+self.itemname+' '+str(self.price)+' ';


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


class Author:
    def __init__(self, authornum, authorname, authorinfo):
        self.authornum = authornum;
        self.authorname = authorname;
        self.authorinfo = authorinfo;

    def __str__(self):
        return str(self.authornum) + ' ' + self.authorname + ' ' + self.authorinfo;


class Itemlist:
    def __init__(self, itemnum, itemname, authorname, price, itemdate, sells):
        self.itemnum = itemnum;
        self.itemname = itemname;
        self.authorname = authorname;
        self.price = price;
        self.itemdate = itemdate;
        self.sells = sells;

    def __str__(self):
        return str(self.itemnum) + ' ' + self.itemname + ' ' + self.authorname + ' ' + \
               str(self.price) + ' ' + str(self.itemdate) + ' ' + self.sells;


class Itemdetail:
    def __init__(self, itemnum, catenum, itemname, price, itemdate, iteminfo, sells, series, authorname, authorinfo):
        self.itemnum = itemnum;
        self.catenum = catenum;
        self.itemname = itemname;
        self.price = price;
        self.itemdate = itemdate;
        self.iteminfo = iteminfo;
        self.sells = sells;
        self.series = series;
        self.authorname = authorname;
        self.authorinfo = authorinfo;

    def __str__(self):
        return str(self.itemnum) + ' ' + str(self.catenum) + ' ' + self.itemname + ' ' + \
               str(self.price) + ' ' + str(self.itemdate) + ' ' + self.iteminfo + ' ' + \
               str(self.sells) + ' ' + str(self.series) + self.authorname + self.authorinfo;


class Orders:
    def __init__(self, ordernum, usernum, totalprice, ordersummary):
        self.ordernum = ordernum;
        self.usernum = usernum;
        self.totalprice = totalprice;
        self.ordersummary = ordersummary;

    def __str__(self):
        return str(self.ordernum)+' '+str(self.usernum)+' '+str(self.totalprice)+' '+self.ordersummary+' ';

class Ordersone:
    def __init__(self, ordernum):
        self.ordernum = ordernum;

    def __str__(self):
        return str(self.ordernum);

class Payment:
    def __init__(self, ordernum, usernum, itemname, paydate, cost):
        self.ordernum = ordernum;
        self.usernum = usernum;
        self.itemname = itemname;
        self.paydate = paydate;
        self.cost = cost;

    def __str__(self):
        return str(self.ordernum)+' '+str(self.usernum)+' '+self.itemname+' '+str(self.paydate)+' '+str(self.cost)+' ';

class Serieslist:
    def __init__(self, itemnum, itemname, price):
        self.itemnum = itemnum;
        self.itemname = itemname;
        self.price = price;

    def __str__(self):
        return str(self.itemnum) + self.itemname + str(self.price);


class Authorlist:
    def __init__(self, authorname, authornum):
        self.authorname = authorname;
        self.authornum = authornum;

    def __str__(self):
        return self.authorname + ' ' + str(self.authornum);


class RecentPublished:
    def __init__(self, itemnum, catenum, itemname, itemdate, price, series):
        self.itemnum = itemnum;
        self.catenum = catenum
        self.itemname = itemname;
        self.itemdate = itemdate;
        self.price = price;
        self.series = series;

    def __str__(self):
        return str(self.itemnum) + ' ' + str(self.catenum) + ' ' + self.itemname + ' ' + \
               str(self.itemdate) + ' ' + str(self.price) + ' ' + str(self.series);



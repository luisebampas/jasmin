class User:
    def __init__(self, id, pwd, name):
        self.id = id;
        self.pwd = pwd;
        self.name = name;

    def __str__(self):
        return self.id + ' ' + self.pwd + ' ' + self.name + ' ';


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

    def __str__(self):
        return str(self.itemnum) + ' ' + self.itemname + ' ' + self.authorname + ' ' + \
               str(self.price) + ' ' + str(self.itemdate);
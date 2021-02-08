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

#class Cartlist:
#    def __init__(self, itemnum, itemname, price):
#        self.itemnum = itemnum;
#       self.itemname = itemname;
#        self.price = price;
#    def __str__(self):
#        return str(self.itemnum)+' '+self.itemname+' '+str(self.price)+' ';
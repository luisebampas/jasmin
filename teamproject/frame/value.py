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


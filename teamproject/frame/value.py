class User:
    def __init__(self, id, pwd, name):
        self.id = id;
        self.pwd = pwd;
        self.name = name;

    def __str__(self):
        return self.id + ' ' + self.pwd + ' ' + self.name + ' ';


class Item:
    def __init__(self, id, name, price, regdate, imgname):
        self.id = id;
        self.name = name;
        self.price = price;
        self.regdate = regdate;
        self.imgname = imgname;

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' \
               + str(self.price) + ' ' + str(self.regdate) + ' ' + self.imgname;

from frame.db import Db
from frame.sql import Sql
from frame.value import User, Orderlist, Mainlist, Cartlist


class UserDb(Db):
    def delete(self, id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userdelete % (id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def update(self, id, pwd, name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userupdate % (pwd, name, id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


    def insert(self, id, pwd, name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userinsert % (id,pwd,name));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def selectone(self,id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlistone % (id) );
        u = cursor.fetchone();
        user = User(u[0],u[1],u[2],u[3]);
        super().close(conn, cursor);
        return user;

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist);
        result = cursor.fetchall();
        all = [];
        for u in result:
            user = User(u[0],u[1],u[2],u[3]);
            all.append(user);
        super().close(conn,cursor);
        return all;

class OrderDb(Db):

    def selectone(self,num):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.orderlistone % (num) );
        result = cursor.fetchall();
        all = [];
        for u in result:
            order = Orderlist(u[0],u[1],u[2]);
            all.append(order)
        super().close(conn, cursor);
        return all;

    def listselectone(self, usernum): # payimpl에 사용
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.orderlistone % int(usernum));
        result = cursor.fetchall();
        all = [];
        for u in result:
            orderlist = Orderlist(u[0],u[1],u[2]);
            all.append(orderlist);
            super().close(conn, cursor);
        return all;

    def mainone(self, num):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.main % num);
        result = cursor.fetchall();
        allm = [];
        for u in result:
            orders = Mainlist(u[0],u[1],u[2],u[3],u[4]);
            allm.append(orders);
        super().close(conn, cursor);
        return allm;

    def listinsert(self, ordernum, usernum, itemnum):  # payimpl에 사용
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.orderlistinsert % (ordernum, usernum, itemnum));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def cart(self, num):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.cart % (num) );
        result = cursor.fetchall();
        allc = [];
        for u in result:
            carts = Cartlist(u[0],u[1],u[2]);
            allc.append(carts)
        super().close(conn, cursor);
        return allc;

    def cartinsert(self, usernum, itemnum):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.cartinsert % (int(usernum), int(itemnum)));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def cartdelete(self, itemnum):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.cartdelete % (itemnum));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


"""
def userlist_test():
    users = UserDb().select();
    for u in users:
        print(u);



def userlistone_test():
    users = UserDb().selectone('id100');
    print(users);
def userinsert_test():
    users = UserDb().insert('id21','pwd21','james21');
def userupdate_test():
    user = UserDb().update('id04','pwd04','james04');
def userdelete_test():
    users = UserDb().delete('id100');
"""

def orderlist_test():
    OrderDb().listinsert(12, 103, 121);


def orderselectone_test():
    orderlist = OrderDb().listselectone(103);
    for u in orderlist:
        print(u);

if __name__ == '__main__':
    userlist_test();
    orderselectone_test();


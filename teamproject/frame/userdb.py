from frame.db import Db
from frame.sql import Sql
from frame.value import User


class UserDb(Db):
<<<<<<< HEAD
    def delete(self, id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userdelete % (id));
=======
    def insert(self, id, pwd, name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userinsert % (id, pwd, name));
>>>>>>> aad851d185dadcdc087b7f21a795bba5c1a79d51
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

<<<<<<< HEAD

    def insert(self, id, pwd, name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userinsert % (id,pwd,name));
=======
    def delete(self, id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userdelete % (id));
>>>>>>> aad851d185dadcdc087b7f21a795bba5c1a79d51
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

<<<<<<< HEAD
    def selectone(self,id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlistone % (id) );
        u = cursor.fetchone();
        user = User(u[0],u[1],u[2],u[3]);
=======
    def selectone(self, id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlistone % id);
        u = cursor.fetchone();
        user = User(u[0], u[1], u[2]);
>>>>>>> aad851d185dadcdc087b7f21a795bba5c1a79d51
        super().close(conn, cursor);
        return user;

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist);
        result = cursor.fetchall();
        all = [];
        for u in result:
<<<<<<< HEAD
            user = User(u[0],u[1],u[2],u[3]);
            all.append(user);
        super().close(conn,cursor);
        return all;




=======
            user = User(u[0], u[1], u[2]);
            all.append(user);
        super().close(conn, cursor);
        return all;


# userlist Test Function ................
>>>>>>> aad851d185dadcdc087b7f21a795bba5c1a79d51
def userlist_test():
    users = UserDb().select();
    for u in users:
        print(u);

<<<<<<< HEAD
def userlistone_test():
    users = UserDb().selectone('id100');
    print(users);
def userinsert_test():
    users = UserDb().insert('id21','pwd21','james21');
def userupdate_test():
    user = UserDb().update('id04','pwd04','james04');
def userdelete_test():
    users = UserDb().delete('id100');

if __name__ == '__main__':
    userlistone_test();
    userlist_test();
=======

def userlistone_test():
    users = UserDb().selectone('id01');
    print(users);


def userinsert_test():
    UserDb().insert('id04', 'pwd04', 'jeams');


def userupdate_test():
    UserDb().update('id01', 'pwd99', '홍말숙');


if __name__ == '__main__':
    userupdate_test();
    userlist_test();
>>>>>>> aad851d185dadcdc087b7f21a795bba5c1a79d51

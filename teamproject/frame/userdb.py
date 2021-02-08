from frame.db import Db
from frame.sql import Sql
from frame.value import User


class UserDb(Db):
    def insert(self, id, pwd, name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userinsert % (id, pwd, name));
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

    def selectone(self, id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlistone % id);
        u = cursor.fetchone();
        user = User(u[0], u[1], u[2]);
        super().close(conn, cursor);
        return user;

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist);
        result = cursor.fetchall();
        all = [];
        for u in result:
            user = User(u[0], u[1], u[2]);
            all.append(user);
        super().close(conn, cursor);
        return all;


# userlist Test Function ................
def userlist_test():
    users = UserDb().select();
    for u in users:
        print(u);


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

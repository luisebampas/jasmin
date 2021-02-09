from frame.db import Db
from frame.sql import Sql
from frame.value import Item, Itemlist, Itemdetail


class ItemDb(Db):
    def insert(self, name,price,imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.iteminsert % (name,price,imgname));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);


    def selectone(self,itemnum):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.itemlistone % int(itemnum));
        i = cursor.fetchone();
        item = Itemdetail(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]);
        super().close(conn, cursor);
        return item;


    def select(self, catenum, page):
        conn = super().getConnection();
        cursor = conn.cursor();
        limit = 20;
        offset = (int(page) - 1) * limit
        cursor.execute(Sql.itemlist + Sql.page % offset);
        result = cursor.fetchall();
        all = [];
        for i in result:
            item = Itemlist(i[0], i[1], i[2], i[3], i[4]);
            all.append(item);
        super().close(conn, cursor);
        return all;


    def update(self,id, name,price, imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.itemupdate % (name,price,imgname,id));
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
            cursor.execute(Sql.itemdelete % (id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

def itemlist_test():
    items = ItemDb().select();
    for i in items:
        print(i);

def itemlistone_test():
    item = ItemDb().selectone(2);
    print(item);


def iteminsert_test():
    ItemDb().insert('shirts',30000,'s.jpg');
def itemupdate_test():
    ItemDb().update(2,'pants2',30000,'s.jpg');
def itemdelete_test():
    ItemDb().delete(2);


if __name__ == '__main__':
    itemlist = ItemDb().select(1, 1);
    for i in itemlist:
        print(i)

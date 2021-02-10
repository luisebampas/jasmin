from frame.db import Db
from frame.sql import Sql
from frame.value import Item, Itemlist, Itemdetail


class ItemDb(Db):
    def insert(self, name, price, imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.iteminsert % (name, price, imgname));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def selectone(self, itemnum):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.itemlistone % int(itemnum));
        i = cursor.fetchone();
        item = Itemdetail(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]);
        super().close(conn, cursor);
        return item;

    def select(self, catenum, page, maxItemlist):
        ordercon = 1;
        offset = (int(page) - 1) * maxItemlist;
        conn = super().getConnection();
        cursor = conn.cursor();
        if catenum == 1:
            catesql = Sql.categoryAll;
        else:
            catesql = Sql.category % catenum;
        if ordercon == 1:
            ordersql = Sql.ordercon1;
        elif ordercon == 2:
            ordersql = Sql.ordercon2;
        elif ordercon == 3:
            ordersql = Sql.ordercon3;
        elif ordercon == 4:
            ordersql = Sql.ordercon4;
        elif ordercon == 5:
            ordersql = Sql.ordercon5;
        elif ordercon == 6:
            ordersql = Sql.ordercon6;
        elif ordercon == 7:
            ordersql = Sql.ordercon7;
        else:
            ordersql = ' ';
        cursor.execute(Sql.itemlist + catesql + ordersql + Sql.page % offset);
        result = cursor.fetchall();
        all = [];
        for i in result:
            item = Itemlist(i[0], i[1], i[2], i[3], i[4]);
            all.append(item);
        super().close(conn, cursor);
        return all;

    def listcount(self, catenum):
        conn = super().getConnection();
        cursor = conn.cursor();
        if catenum == 1:
            catesql = Sql.categoryAll;
        else:
            catesql = Sql.category % catenum;
        cursor.execute(Sql.itemlistcount + catesql)
        count = cursor.fetchone()[0];
        return count;

    def update(self, id, name, price, imgname):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.itemupdate % (name, price, imgname, id));
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


if __name__ == '__main__':
    """
    itemlist = ItemDb().select(1, 1);
    for i in itemlist:
        print(i)
    """
    itemlistcount = ItemDb().listcount(1);
    print(itemlistcount);
from frame.db import Db
from frame.sql import Sql
from frame.value import Item, Itemlist, Itemdetail, Orders, Payment, Ordersone, RecentPublished


class ItemDb(Db):
    def insert(self, catenum, authornum, itemname, price, itemdate, iteminfo, sells, series):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.iteminsert % (catenum, authornum, itemname, price, itemdate, iteminfo, sells, series));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def getautoincre(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.itemautoincre);
        i = cursor.fetchone();
        autoincre = i[0];
        super().close(conn, cursor);
        return autoincre;

    def selectone(self, itemnum):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.itemlistone % int(itemnum));
        i = cursor.fetchone();
        item = Itemdetail(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]);
        super().close(conn, cursor);
        return item;

    def select(self, catenum, page, maxItemlist, searchmod=1, searchword='', ordercon=1):
        offset = (int(page) - 1) * maxItemlist;
        conn = super().getConnection();
        cursor = conn.cursor();
        if catenum == 1:
            catesql = Sql.categoryAll;
        else:
            catesql = Sql.category % catenum;

        if searchmod == 1:
            searchsql = Sql.searchAll + searchword + "%'"
        elif searchmod == 2:
            searchsql = Sql.searchWithTitle + searchword + "%'"
        elif searchmod == 3:
            searchsql = Sql.searchWithAuthor + searchword + "%'"
        else:
            searchsql = '';

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
        cursor.execute(Sql.itemlist + catesql + searchsql + ordersql + Sql.page % (maxItemlist, offset));
        result = cursor.fetchall();
        all = [];
        for i in result:
            item = Itemlist(i[0], i[1], i[2], i[3], i[4], i[5]);
            all.append(item);
        super().close(conn, cursor);
        return all;

    def selectall(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.itemlist);
        result = cursor.fetchall();
        all = [];
        for i in result:
            item = Itemlist(i[0],i[1],i[2],i[3],i[4],i[5]);
            all.append(item);
        super().close(conn,cursor);
        return all;

    def listcount(self, catenum, searchmod=1, searchword=''):
        conn = super().getConnection();
        cursor = conn.cursor();
        if catenum == 1:
            catesql = Sql.categoryAll;
        else:
            catesql = Sql.category % catenum;
        if searchmod == 1:
            searchsql = Sql.searchAll + searchword + "%'"
        elif searchmod == 2:
            searchsql = Sql.searchWithTitle + searchword + "%'"
        elif searchmod == 3:
            searchsql = Sql.searchWithAuthor + searchword + "%'"
        else:
            searchsql = '';
        cursor.execute(Sql.itemlistcount + catesql + searchsql)
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

    def sellitem(self, itemnum):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.sellitem % int(itemnum));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def recentPublished(self, authornum, limit):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recentPublished % (authornum, limit));
        result = cursor.fetchall();
        all = [];
        for i in result:
            idate = i[3].strftime('%Y-%m-%d');
            pubs = RecentPublished(i[0], i[1], i[2], idate, i[4], i[5],);
            all.append(pubs);
        super().close(conn, cursor);
        return all;


class OrdersDb(Db):

    def insert(self, usernum, itemnum, odersummary):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.ordersinsert % (int(usernum), int(itemnum), odersummary));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.ordersselect);
        result = cursor.fetchall();
        all = [];
        for u in result:
            order = Orders(u[0], u[1], u[2], u[3]);
            all.append(order);
        super().close(conn, cursor);
        return all;

    def selectone(self, usernum):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.odersselectone % int(usernum));
        result = cursor.fetchone();
        ordernum = str(result[0]);
        super().close(conn, cursor);
        return ordernum;

class PaymentDb(Db):
    def insert(self, ordernum, usernum, itemname, cost):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.paymentinsert % (int(ordernum), int(usernum), itemname, int(cost)));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist);
        result = cursor.fetchall();
        all = [];
        for u in result:
            payment = Payment(u[0], u[1], u[2], u[3], u[4]);
            all.append(payment);
        super().close(conn, cursor);
        return all;

    def selectone(self, usernum):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.paymentselectone % usernum);
        result = cursor.fetchall();
        all = [];
        for u in result:
            payone = Payment(u[0], u[1], u[2], u[3], u[4]);
            all.append(payone);
        super().close(conn, cursor);
        return all;



if __name__ == '__main__':
    """
    itemlist = ItemDb().select(1, 1);
    for i in itemlist:
        print(i)
    
    itemlistcount = ItemDb().listcount(1);
    print(itemlistcount);
    """
    """
    catenum = 2; authornum = 1; itemname = '테스트'; price = 9999; itemdate = '2021-02-15'; iteminfo = '시리즈테스트용';
    sells = 0; series = 0;
    auto = ItemDb().insert(catenum, authornum, itemname, price, itemdate, iteminfo, sells, series);
    """
    test = ItemDb().getautoincre();
    print(test)
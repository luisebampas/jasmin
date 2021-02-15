from frame.db import Db
from frame.sql import Sql
from frame.value import Authorlist


class AuthorDb(Db):
    def insert(self, name, info):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.authorinsert % (name, info));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def searchauthor(self, search_authorname):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.searchAuthorNameFront + search_authorname + Sql.searchAuthorNameRear);
        result = cursor.fetchall();
        all = [];
        for i in result:
            author = Authorlist(i[0], i[1]);
            all.append(author);
        super().close(conn, cursor);
        return all;
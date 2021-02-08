import MySQLdb

config = {
<<<<<<< HEAD
    'database':'jasmine',
    'user':'root',
    'password':'111111',
    'host':'127.0.0.1',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

class Db:
    def getConnection(self):
        conn = MySQLdb.connect(**config);
        return conn;

    def close(self, conn, cursor):
        if cursor != None:
            cursor.close();
        if conn != None:
            cursor.close();
=======
    'database': 'jasmindb',
    'user': 'root',
    'password': '111111',
    'host': '127.0.0.1',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}


class Db:
    def getConnection(self):
        conn = MySQLdb.connect(**config)
        return conn

    def close(self, conn, cursor):
        if cursor != None:
            cursor.close()
        if conn != None:
            cursor.close()
>>>>>>> aad851d185dadcdc087b7f21a795bba5c1a79d51

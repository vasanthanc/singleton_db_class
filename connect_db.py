import mysql.connector as MySQLdb
from time import sleep


class ConnectDB (object):
    """
    Singleton class
    """
    _instance = None
    config = {
        'user': 'root',
        'host': '127.0.0.1',
        'database': 'classicmodels',
    }

    def __new__(cls):
        if ConnectDB._instance == None:
            ConnectDB._instance = object.__new__ (cls)
            try:
                print ("Connecting to Database {}".format (ConnectDB.config.get ("database", None)))
                connection = ConnectDB._instance.connection = MySQLdb.connect (**cls.config)
                cursor = ConnectDB._instance.cursor = connection.cursor ()
                cursor.execute ('SELECT VERSION()')
                db_version = cursor.fetchone ()
                # print ("Version {}".format (db_version))
            except Exception as error:
                print ('Error: connection not established {}'.format (error))
                ConnectDB._instance = None
            else:
                print ("Connection Established")
        else:
            print ("Using Existing connection")
        return cls._instance

    def __init__ (self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor


    # def __exit__(self, exc_type, exc_val, exc_tb):
    #   if self.connection:
    #     self.connection.close()
    #   if self.cursor:
    #     self.cursor.close()
    #
    # def __enter__(self):
    #   return self


if __name__ == "__main__":
    d = ConnectDB()
    # with ConnectDB() as d:
    c = d.cursor
    c.execute ("SHOW TABLES")
    print (c.fetchall ())
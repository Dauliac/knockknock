#!/usr/bin/python
# coding: utf-8
class Connection():
    def __init__(self, user, password, host, database, tries=3):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.tries = tries
        self.connect = None

    def connect(self, tries):
        if not tries:
            tries = self.tries
        try:
            connection = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             db=self.database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            cnx = mysql.connector.connect(**self.config)
            print('sql connection: ok')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                self.status = True
                return False
        except mysql.connector.InterfaceError:
            if tries == 0:
                self.status = None
                return None
            self.connector(tries-1)

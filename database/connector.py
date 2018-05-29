class Connection():
"""
    Mysql connection object:
        - config: 
        - tries: integer
        - connect: boolean
"""

    def __init__(self, user, password, host, database, tries=3):
        self.config = {
            'user': user,
            'password': password,
            'host': host,
            'database': database
        }
        self.tries = tries
        self.connect = None

    def connect(self, tries=self.tries):
        """
            call to connect to mysql database
        """
        try:
            cnx = mysql.connector.connect(**config)
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

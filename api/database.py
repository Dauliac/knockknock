"""
    Author      : github.com/TonyChG
    Date        : Sat 02 Jun 2018 04:21:53 PM CEST
    Description : 
    Usage       :

"""

from flaskext.mysql import MySQL

class User:
    def __init__(self):
        self.cursor = client.get_db().cursor()

class Ringtone:
    def __init__(self):
        self.cursor = client.get_db().cursor()

class Client:
    def __init__(self, app):
        mysql = MySQL()
        mysl.init_app(app)


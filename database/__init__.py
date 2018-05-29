"""
    Author      : github.com/TonyChG
    Date        : Tue 29 May 2018 04:47:25 PM CEST
    Description : 
    Usage       :

"""

from database.users import Users
from app.constants import SQL_USER, SQL_USER, SQL_DB, SQL_PWD, SQL_HOST
from database.ringtones import Ringtones
from database.connector import Connection

# test Conenction
client = Connection(SQL_USER, SQL_PWD, SQL_HOST, SQL_DB)
client.connect();

users = Users(client)
ringtones = Ringtones(client)


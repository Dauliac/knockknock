"""
    Author      : github.com/TonyChG
    Date        : Tue 29 May 2018 04:47:25 PM CEST
    Description : 
    Usage       :

"""

from database.users import Users
from database.ringtones import Ringtones
from database.connector import Connection

client = Connection("admin", "password", "0.0.0.0", "knockknock")
users = Users(client)
ringtones = Ringtones(client)


#!/usr/bin/python
# coding: utf-8
import pymysql.cursors
from pymysql.err import OperationalError
from pymysql import InternalError
class Connection():
    def __init__(self, user, password, host, database, tries=2):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.tries = tries
        self.status = None

    def connect(self, tries=None):
        if not tries:
            tries = self.tries
        connection = pymysql.connect(host=self.host,
                         user=self.user,
                         password=self.password,
                         db=self.database,
                         #  charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)
        self.status = True
        print('sql connection: ok')

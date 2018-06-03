#!/usr/bin/env python3.5
"""
    Author      : github.com/TonyChG
    Date        : Sat 02 Jun 2018 09:45:48 PM CEST
    Description : 
    Usage       :

"""

import mysql.connector
from flask import g, current_app as app

class Repository:
    def __init__(self):
        self.client = self.get_db()
        self.cursor = self.client.cursor()
        self.private = []
        self.keys = ['id']
        self.table = ''

    def get_db(self):
        if 'mysql_client' not in g:
            g.mysql_client = mysql.connector.connect(
                    host=app.config['MYSQL_HOST'],
                    user=app.config['MYSQL_USER'],
                    password=app.config['MYSQL_PASSWORD'],
                    database=app.config['MYSQL_DATABASE']
                    )
        return g.mysql_client

    def init_cursor(self):
        if not self.cursor:
            self.cursor = self.client.cursor()

    def serialize(self, row, filter=False):
        if not row:
            return None
        obj = {}
        for i in range(len(self.keys)):
            key = self.keys[i]
            if not filter or filter and (key not in self.private):
                obj[key] = row[i]
            else:
                obj[key] = ''
        return obj

    def findall(self, filter=False):
        results = self.results("select * from {}".format(self.table))
        collection = []
        for item in results:
            collection.append(self.serialize(item, filter))
        return collection
    
    def find(self, condition, filter=False):
        item = self.findone("select * from {} where {}".format(self.table, condition))
        return self.serialize(item, filter)

    def findone(self, querystring):
        self.init_cursor()
        self.cursor.execute(querystring)
        results = self.cursor.fetchall()
        if len(results) > 0:
            return results[0]
        return None
 
    def results(self, querystring):
        self.init_cursor()
        self.cursor.execute(querystring)
        return self.cursor.fetchall()

    def commit(self, querystring):
        self.init_cursor()
        self.cursor.execute(querystring)
        return self.client.commit()


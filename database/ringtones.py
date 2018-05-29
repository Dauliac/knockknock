#!/usr/bin/python
# coding: utf-8

import pymysql.cursors

class Ringtones:
    def __init__(self, client):
        self.result = None
        self.client = client

    def find_all(self):
        try:
            sql = "SELECT * FROM `ringtones`"
            client = self.client
            cursor.execute(sql, (id))
            self.result = cursor.fetchone()
            return self.result
        except:
            print('mysql connection lost')
            try:
                self.client.connect()
                self.find_by_id(id)
            except:
                return False
                print('sql connection crashed')

    def find_by_id(self, id):
        try:
            sql = "SELECT * FROM `ringtones` WHERE `id`=%s"
            cursor.execute(sql, (id))
            self.result = cursor.fetchone()
            return self.result
        except:
            print('mysql connection lost')
            try:
                self.client.connection()
                self.find_by_id(id)
            except:
                return False
                print('sql connection crashed')

    def post(status, replay_url):
        try:
            sql = ("INSERT INTO ringtones "
                    "(status, replay_url) "
                    "VALUES (%s, %s)")
            cursor.execute(sql, (status, replay_url))
            connection.commit()
            return True
        except:
            print('mysql connection lost')
            try:
                self.client.connect()
                self.post(email, password, admin_level)
            except:
                return False
                print('sql connection crashed')

    def delete(self, id):
        try:
            sql = ("INSERT INTO users "
                    "(email, password, admin_level) "
                    "VALUES (%s, %s, %s)")
            cursor.execute(sql, (email, password, admin_level))
            self.result = cursor.fetchall()
            connection.commit()
            return True
        except:
            print('mysql connection lost')
            try:
                self.client.connect()
                self.post(email, password, admin_level)
            except:
                return False
                print('sql connection crashed')

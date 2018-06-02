#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:23:09 AM CEST
    Description : 
    Usage       :

"""
#  from connector import Connection

from hashlib import sha256

class Users:
    """
        User database interface.
    """
    def __init__(self, client):
        self.result = None

    def get_by_id(self, id):
        try:
            sql = "SELECT * FROM `users` WHERE `id`=%s"
            cursor.execute(sql, (id))
            self.result = cursor.fetchone()
        except mysql.connector.InterfaceError as err:
            print('mysql connection lost')
            try:
                database.connection()
                self.get_by_id(id)
            except:
                print('sql connection crashed')

    def get_by_email(self, email):
        try:
            sql = "SELECT * FROM `users` WHERE `email`=%s"
            cursor.execute(sql, (email))
            self.result = cursor.fetchone()
        except mysql.connector.InterfaceError as err:
            print('mysql connection lost')
            database.connection()
            try:
                database.connection()
                self.get_by_email(email)
            except:
                print('sql connection crashed')

    def post(self, email, password, admin_level):
        try:
            sql = ("INSERT INTO users "
                    "(email, password, admin_level) "
                    "VALUES (%s, %s, %s)")
            cursor.execute(sql, (email, sha256(password).hexdigest(), admin_level))
            self.result = cursor.fetchone()
        except mysql.connector.InterfaceError as err:
            print('mysql connection lost')
            database.connection()
            try:
                database.connection()
                self.get_by_id(id)
            except:
                print('sql connection crashed')

    #  def set_email(self, id, email):
    #  def set_password(self, id, email):
    #  def set_admin_level(self, id, email):
    #  def set_token(self, id, token):
    #  def set_last_login(self, id)

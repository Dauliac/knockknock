#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:23:09 AM CEST
    Description : 
    Usage       :

"""
#  from connector import Connection

class Users:
    """
        User database interface.
    """
    def __init__(self):
        self.result = None
    
    def find_all(self):
        try:
            sql = "SELECT * FROM `users`"
            cursor.execute(sql, (id))
            self.result = cursor.fetchone()
            return self.result
        except mysql.connector.InterfaceError as err:
            print('mysql connection lost')
            try:
                database.connection()
                self.find_by_id(id)
            except:
                return False
                print('sql connection crashed')


    def find_by_id(self, id):
        try:
            sql = "SELECT * FROM `users` WHERE `id`=%s"
            cursor.execute(sql, (id))
            self.result = cursor.fetchone()
            return self.result
        except mysql.connector.InterfaceError as err:
            print('mysql connection lost')
            try:
                database.connection()
                self.find_by_id(id)
            except:
                return False
                print('sql connection crashed')

    def find_by_email(email):
        try:
            sql = "SELECT * FROM `users` WHERE `email`=%s"
            cursor.execute(sql, (email))
            self.result = cursor.fetchall()
            return self.result
        except mysql.connector.InterfaceError as err:
            print('mysql connection lost')
            database.connection()
            try:
                database.connection()
                self.find_by_email(email)
            except:
                return False
                print('sql connection crashed')

    def post(email, password, admin_level):
        try:
            sql = ("INSERT INTO users "
                    "(email, password, admin_level) "
                    "VALUES (%s, %s, %s)")
            cursor.execute(sql, (email, password, admin_level))
            self.result = cursor.fetchall()
            connection.commit()
            return True
        except mysql.connector.InterfaceError as err:
            print('mysql connection lost')
            try:
                database.connection()
                self.post(email, password, admin_level)
            except:
                return False
                print('sql connection crashed')

    #  def set_email(self, id, email):
    #  def set_password(self, id, email):
    #  def set_admin_level(self, id, email):
    #  def set_token(self, id, token):
    #  def set_last_login(self, id)

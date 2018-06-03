"""
    Author      : github.com/TonyChG
    Date        : Sat 02 Jun 2018 09:09:22 PM CEST
    Description : 
    Usage       :

"""

from hashlib import sha256
from database.models.Repository import Repository

class User(Repository):
    def __init__(self):
        Repository.__init__(self)
        self.table = 'users'
        self.keys = [
                'id', 
                'email', 
                'password', 
                'auth_token', 
                'admin_level', 
                'last_login', 
                'created_at'
                ]
        self.private = [
                'password',
                'auth_token',
                'admin_level'
                ]

    def flush(self):
        return self.commit('truncate users')

    def findby_id(self, id):
        return self.find("id = '{}'".format(id))

    def findby_email(self, email):
        return self.find("email = '{}'".format(email))

    def create(self, email, password):
        password = sha256(password.encode('utf-8')).hexdigest()
        querystring = "insert into users(email, password, admin_level, created_at, last_login) values ('{}', '{}', 0, NOW(), NOW())"
        return self.commit(querystring.format(email, password))

    def update(self, user):
        req_user = self.serialize(self.findby_id(user['id']))
        querystring = "update users set"
        values = []
        for key in self.keys[1:]:
            if key in user and req_user[key] != user[key]:
                values.append(" {} = '{}'".format(key, user[key]))
        querystring += ((',').join(tuple(values)))
        querystring += " where id = {}".format(user['id'])
        if len(values) > 0:
            self.commit(querystring)
        return self.serialize(self.findby_id(user['id']), True)

    def remove(self, id):
        querystring = "delete from {} where id = {}"
        return self.commit(querystring.format(self.table, id))

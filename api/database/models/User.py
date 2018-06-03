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

    def serializeList(self, users, filters=[]):
        serialized_users = []
        for user in users:
            serialized_users.append(self.serialize(user, filters))
        return serialized_users

    def serialize(self, user, filter=False, filters=[]):
        if filter == True:
            filters = self.private
        dict_user = {}
        index = 0
        for key in self.keys:
            if user[index] and not (filter and key in filters):
                dict_user[key] = user[index]
            elif not key in filters:
                dict_user[key] = ''
            index += 1
        return dict_user

    def flush(self):
        return self.commit('truncate users')

    def findall(self, filters=[]):
        return self.serializeList(self.results('select * from users'), filters)

    def findby_id(self, id):
        return self.findone("select * from users where id = '{}'".format(id))

    def findby_email(self, email):
        user = self.findone("select * from users where email = '{}'".format(email))
        return self.serialize(user)

    def create(self, email, password):
        password = sha256(password.encode('utf-8')).hexdigest()
        querystring = "insert into users(email, password, admin_level, created_at) values ('{}', '{}', 0, NOW())"
        return self.commit(querystring.format(email, password))

    def update(self, user):
        req_user = self.serialize(self.findby_id(user['id']))
        querystring = 'update users'
        changing = False
        for key in user:
            if key not in self.keys:
                return None
            else:
                if req_user[key] != user[key]:
                    changing = True
                    querystring += " set {} = '{}'".format(key, user[key])
        querystring += " where id = {}".format(user['id'])
        self.commit(querystring)

        return self.findby_email(req_user['email'])

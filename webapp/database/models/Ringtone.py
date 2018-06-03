"""
    Author      : github.com/TonyChG
    Date        : dim. 03 juin 2018 17:35:40 CEST
    Description : 
    Usage       :

"""

from database.models.Repository import Repository

class Ringtone(Repository):
    def __init__(self):
        Repository.__init__(self)
        self.table = 'users'
        self.keys = [
                'id', 
                'status', 
                'replay_url', 
                'timestamp', 
                ]

    def flush(self):
        return self.commit('truncate users')

    def findby_id(self, id):
        return self.find("id = '{}'".format(id))

    def create(self, email, password):
        return

    def update(self, ringtone):
        # req_user = self.serialize(self.findby_id(user['id']))
        # querystring = "update users set"
        # values = []
        # for key in self.keys[1:]:
        #     if key in user and req_user[key] != user[key]:
        #         values.append(" {} = '{}'".format(key, user[key]))
        # querystring += ((',').join(tuple(values)))
        # querystring += " where id = {}".format(user['id'])
        # if len(values) > 0:
        #     self.commit(querystring)
        # return self.serialize(self.findby_id(user['id']), True)
        return ringtone

    def remove(self, id):
        querystring = "delete from {} where id = {}"
        return self.commit(querystring.format(self.table, id))


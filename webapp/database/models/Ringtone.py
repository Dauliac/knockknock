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
        self.table = 'ringtones'
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

    def remove(self, id):
        querystring = "delete from {} where id = {}"
        return self.commit(querystring.format(self.table, id))

    def update_status(self, id, status):
        querystring = "update ringtones set status = '{}' where id = {}"
        return self.commit(querystring.format(status, id))

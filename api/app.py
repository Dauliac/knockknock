#! /usr/bin/python3.6
# -*- coding:utf-8 -*-

from flask import Flask, jsonify, g
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
import bcrypt
import mysql.connector

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')

#################################
#        DB CONNECTIONS
#################################
def connect_db():
	g.mysql_connection = mysql.connector.connect(
		host = app.config['DATABASE_HOST'],
		user = app.config['DATABASE_USER'],
		password = app.config['DATABASE_PASSWORD'],
		database = app.config['DATABASE_NAME']
	)
	g.mysql_cursor = g.mysql_connection.cursor()
	return g.mysql_cursor

def get_db () :
    if not hasattr(g, 'db') :
        g.db = connect_db()
    return g.db

def commit():
	g.mysql_connection.commit()

@app.teardown_appcontext
def close_db (error) :
    if hasattr(g, 'db') :
        g.db.close()

#################################
#        JWT
#################################

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

"""
class User(Resource):
	def get_all(self):
		//

	def get(self, user_id):
		//

	def post(self):
		//

	def put(self, user_id):
		//

	def delete(self, user_id):
		//

class History(Resource):
	def get(self):
		//

	def post(self):
		//

	def put(self):
		//

	def delete(self):
		//

@app.route('/register/'):
	def register():
		//

@app.route('/login/', methods = ['GET', 'POST']):
	def login():
		//

@app.route('/logout/'):
	def logout():
		//

@app.route('/ring/'):
	def ring():
		//

@app.route('/admin/'):
	def admin():
		//

api.add_resource(User, '/user/')
api.add_resource(History, '/history/')
"""
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', use_reloader=False)
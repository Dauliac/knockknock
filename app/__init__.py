#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:30:54 AM CEST
    Description : 
    Usage       :

"""

import jwt
from flask import Flask, render_template, jsonify, request, session
from hashlib import sha256
from app.constants import JWT_SECRET, JWT_ALGORITHM
from app.api.errors import error_response
from flask_socketio import send, emit, SocketIO
from app.api import api
import pymysql.cursors
from database import users, ringtones

app = Flask(__name__)
app.config.from_object('config')
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login():
    email = request.form['email'].encode('utf-8')
    password = request.form['password'].encode('utf-8')
    passhash = sha256(password).hexdigest()

    user = users.find_by_email(email)
    print(user)
    user = {
        'email': 'admin@example.com',
        'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    }
    if user['password'] == passhash:
        token = jwt.encode({ 'user': user['email'] }, JWT_SECRET, JWT_ALGORITHM)
        session[user['email']] = token
        #  return jsonify({ 'token': token })
        return render_template('index.html', token=token)
    else:
        return error_response(401, 'Invalid credentials')

# @socketio.on('connected')
def handle_connection(data):
    emit('customEmit')
    emit('customEmit', jsonify({ 'useremail': user['email'], 'token': token }))
    # print(data)

def run(host):
    app.register_blueprint(api, url_prefix='/api')
    socketio.on_event('connected', handle_connection)
    socketio.run(app, host=host)


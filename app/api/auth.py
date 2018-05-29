#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:18:16 AM CEST
    Description : 
    Usage       :

"""

import jwt
from flask import request, jsonify, abort, session, render_template
from app.api import api
from hashlib import sha256
from app.constants import JWT_SECRET, JWT_ALGORITHM
from app.api.errors import error_response

@api.route('/login', methods=['POST'])
def login():
    # Todo: Find user in database
    user = {
        'email': 'admin@example.com',
        'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    }
    email = request.form['email'].encode('utf-8')
    password = request.form['password'].encode('utf-8')
    passhash = sha256(password).hexdigest()

    if user['password'] == passhash:
        token = jwt.encode({ 'user': user['email'] }, JWT_SECRET, JWT_ALGORITHM)
        session[user['email']] = token
        # return jsonify({ 'token': token })
        return render_template('index.html', token=token)
    else:
        return error_response(401, 'Invalid credentials')

@api.route('/authenticated', methods=['GET'])
def authenticated(): 
    token = request.headers.get('Authorization')
    if token:
        decode = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        if decode['user'] in session:
            print(session[decode['user']])
        return jsonify({ 'message': 'Authenticated' })
    return error_response(401, 'Unauthorized')

@api.route('/logout', methods=['DELETE'])
def logout():
    pass


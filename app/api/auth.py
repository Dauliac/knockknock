#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:18:16 AM CEST
    Description : 
    Usage       :

"""

import jwt
from flask import request, jsonify, abort, session
from app.api import api
from hashlib import sha256
from app.constants import JWT_SECRET, JWT_ALGORITHM
from app.api.errors import error_response
from database.users import Users as users_model

@api.route('/login', methods=['POST'])
def login():
    user = {
        'email': 'admin@example.com',
        'password': 'admin'
    }
    users = users_model()
    email = request.form['email'].encode('utf-8')
    users.find_by_email(email)
    password = request.form['password'].encode('utf-8')
    passhash = sha256(password).hexdigest()

    if user['password'] == passhash:
        token = jwt.encode({ 'user': user['email'] }, JWT_SECRET, JWT_ALGORITHM)
        return jsonify({ 'token': token })
    else:
        return error_response(401, 'Invalid credentials')

@api.route('/authenticated', methods=['GET'])
def authenticated(): 
    token = request.headers.get('Authorization')
    if token:
        decode = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return jsonify({ 'message': 'Authenticated' })
    return error_response(401, 'Unauthorized')

@api.route('/logout', methods=['DELETE'])
def logout():
    pass


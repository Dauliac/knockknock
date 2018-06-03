"""
    Author      : github.com/TonyChG
    Date        : Sat 02 Jun 2018 07:47:57 PM CEST
    Description : 
    Usage       :

"""

from flask import (
        Blueprint, request, session, jsonify
        )
from database import get_models
from .error import error_response
from hashlib import sha256
import time
import jwt

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['GET'])
def users():
    models = get_models()
    User = models.get('User')
    users = User.findall(filters=['password', 'auth_token', 'admin_level'])
    return jsonify(users)

@bp.route('/login', methods=['POST'])
def login():
    models = get_models()
    User = models.get('User')

    usermail = str(request.form['email'])
    password = request.form['password'].encode('utf-8')
    user = User.findby_email(usermail)

    if not user:
        return error_response('Wrong credentials', 401)
    if user['password'] == sha256(password).hexdigest():
        token = jwt.encode({
            'email': user['email'],
            }, 'secret', algorithm='HS256')
        user['last_login'] = time.strftime('%Y-%m-%d %H:%M:%S')
        print(User.update(user))
        return jsonify({ 'token': str(token.decode('utf-8')) })
    return error_response('Wrong credentials', 401)

@bp.route('/register', methods=['POST'])
def register():
    return jsonify({})

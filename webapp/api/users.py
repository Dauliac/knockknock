"""
    Author      : github.com/TonyChG
    Date        : dim. 03 juin 2018 14:41:11 CEST
    Description : 
    Usage       :

"""

from flask import (
        Blueprint, request, session, jsonify
        )
from database import get_models
from .error import error_response

bp = Blueprint('api_users', __name__, url_prefix='/api/users')

@bp.route('/', methods=['GET'])
def find_all():
    models = get_models()
    User = models.get('User')
    users = User.findall(filter=True)
    return jsonify(users)

@bp.route('/<id>', methods=['GET'])
def find_one(id):
    models = get_models()
    User = models.get('User')
    user = User.findby_id(id)
    if not user:
        return error_response('Not found', 404)
    return jsonify(User.serialize(user, True))

@bp.route('/<id>', methods=['PUT'])
def update(id):
    models = get_models()
    User = models.get('User')
    updateUser = {
            'id': id,
            'email': request.form['email'],
            'admin_level': int(request.form['admin_level']),
            'auth_token': request.form['auth_token']
            }
    updateUser = User.update(updateUser)

    return jsonify(updateUser)

@bp.route('/create', methods=['POST'])
def create():
    models = get_models()
    User = models.get('User')
    if 'email' not in request.form or 'password' not in request.form:
        return error_response('Invalid form', 301)
    usermail = request.form['email']
    password = request.form['password']
    new_user = User.create(usermail, password)
    return jsonify(User.serialize(User.findby_email(usermail), True))

@bp.route('/<id>', methods=['DELETE'])
def remove(id):
    models = get_models()
    User = models.get('User')
    user = User.findby_id(id)
    if not user:
        return error_response('Not found.', 404)
    if User.remove(id):
        return error_response('Error on delete.', 400)
    return jsonify({ 'status': 'Success' })

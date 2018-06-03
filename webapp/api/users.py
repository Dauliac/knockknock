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
    users = User.findall(filters=['password', 'auth_token', 'admin_level'])
    return jsonify(users)

@bp.route('/')

"""
    Author      : github.com/TonyChG
    Date        : dim. 03 juin 2018 17:43:00 CEST
    Description : 
    Usage       :

"""

from flask import (
        Blueprint, request, session, jsonify
        )
from database import get_models
from .error import error_response

# Ringtone STATUS
PENDING=1
UP=2
OPEN=3
CLOSE=4
TIMEOUT=5

bp = Blueprint('api_ringtones', __name__, url_prefix='/api/ringtones')
def get_model():
    models = get_models()
    return models.get('Ringtone')

@bp.route('/', methods=['GET'])
def find_all():
    Ringtone = get_model()
    ringtones = Ringtone.findall()

    return jsonify(ringtones)

@bp.route('/<id>', methods=['PUT'])
def update_pending(id):
    Ringtone = get_model()
    ringtone = Ringtone.serialize(Ringtone.findby_id(id))
    if ringtone and 'status' in ringtone and ringtone.get('status') == 1:
        Ringtone.update_status(id, int(request.form['status']))
        return jsonify({ 'status': 'Success' })
    return error_response('Error on update', 400)

@bp.route('/pending', methods=['GET'])
def find_pending():
    Ringtone = get_model()
    ringtones = Ringtone.findall(False, "status = '{}'".format(PENDING))
    if not len(ringtones):
        return error_response('No pending events.', 201)
    return jsonify(ringtones)

@bp.route('/<id>', methods=['GET'])
def find_one(id):
    Ringtone = get_model()
    ringtone = Ringtone.findby_id(id)
    if not ringtone:
        return error_response('Not found', 404)
    return jsonify(Ringtone.serialize(ringtone))

@bp.route('/<id>', methods=['DELETE'])
def remove(id):
    Ringtone = get_model()
    ringtone = Ringtone.findby_id(id)
    if not ringtone:
        return error_response('Not found', 404)
    if Ringtone.remove(id):
        return error_response('Error on delete', 400)
    return jsonify({ 'status': 'Success' })


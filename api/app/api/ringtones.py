#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:23:09 AM CEST
    Description : 
    Usage       :

"""
from flask import jsonify
from app.api import api
import datetime

current_date = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

@api.route('/ringtones', methods=['GET'])
def list_ringtones():
    # List all ringtones
    db.execute("SELECT id, status, replay_url, timestamp FROM events")
    ringtones = db.fetchall()
    return jsonify(ringtones)

@api.route('/ringtones/<int:id>', methods=['GET'])
def get_ringtone(id):
    # Get ringtone by id
    db.execute("SELECT id, status, replay_url, timestamp FROM events WHERE id = ('%s')" % (id))
    ringtone = db.fetchone()
    return jsonify(ringtone)

@api.route('/ringtones/<int:id>', methods=['PUT'])
def update_ringtone(id):
    # Update ringtone by id
    if request.method == 'PUT':
        data = request.get_json()
        db.execute("UPDATE events SET status=('%s'), replay_url=('%s'), timestamp=('%s') WHERE id=('%s')" % 
            (data['status'], data['replay_url'], current_date, id))
        return Response('Ringtone updated', status=200)
    else:
        return Response('Bad request', status=400)

@api.route('/ringtones', methods=['POST'])
def create_ringtone():
    # Create new ringtone
    if request.method == 'POST':
        data = request.get_json()
        db.execute("INSERT INTO events (status, replay_url, timestamp) VALUES ('%s'),('%s'),('%s')" %
            (data['status'], data['replay_url'], current_date))
        return Response('Ringtone created', status=201)
    else:
        return Response('Bad request', status=400)

@api.route('/ringtones/<int:id>', methods=['DELETE'])
def delete_ringtone(id):
    # Delete ringtone by id
    if request.method == 'DELETE':
        db.execute("DELETE FROM events WHERE id = ('%s')" % id)
        return Response('Ringtone deleted', status=200)
    else:
        return Response('Bad request', status=400)
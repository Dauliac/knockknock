#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:23:09 AM CEST
    Description : 
    Usage       :

"""

from app.api import api

@api.route('/events', methods=['GET'])
def list_events():
    # List all events
    pass

@api.route('/events/<int:id>', methods=['GET'])
def get_event():
    # Get event by id
    pass

@api.route('/events/<int:id>', methods=['PUT'])
def update_event():
    # Update event by id
    pass

@api.route('/events', methods=['POST'])
def create_event():
    # Create new event
    pass

@api.route('/events/<int:id>', methods=['DELETE'])
def delete_event():
    # Delete event by id
    pass

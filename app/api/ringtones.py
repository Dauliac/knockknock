#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:23:09 AM CEST
    Description : 
    Usage       :

"""

from app.api import api

@api.route('/ringtones', methods=['GET'])
def list_ringtones():
    # List all ringtones
    pass

@api.route('/ringtones/<int:id>', methods=['GET'])
def get_ringtone():
    # Get ringtone by id
    pass

@api.route('/ringtones/<int:id>', methods=['PUT'])
def update_ringtone():
    # Update ringtone by id
    pass

@api.route('/ringtones', methods=['POST'])
def create_ringtone():
    # Create new ringtone
    pass

@api.route('/ringtones/<int:id>', methods=['DELETE'])
def delete_ringtone():
    # Delete ringtone by id
    pass

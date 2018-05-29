#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:23:09 AM CEST
    Description : 
    Usage       :

"""

from app.api import api

@api.route('/users', methods=['GET'])
def list_users():
    pass

@api.route('/users/<int:id>', methods=['GET'])
def get_user():
    # Get user by id
    pass

@api.route('/users/<int:id>', methods=['PUT'])
def update_user():
    # Update user by id
    pass

@api.route('/users', methods=['POST'])
def create_user():
    # Create new user
    pass

@api.route('/users/<int:id>', methods=['DELETE'])
def delete_user():
    # Delete user by id
    pass


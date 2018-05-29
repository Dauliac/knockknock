#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:18:16 AM CEST
    Description : 
    Usage       :

"""

from app.api import api

@api.route('/login', methods=['POST'])
def login():
    # Validate login form
    pass

@api.route('/logout', methods=['DELETE'])
def logout():
    # Delete token
    pass

@api.route('/register', methods=['POST'])
def register():
    # Create user
    pass

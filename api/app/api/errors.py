#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:29:10 AM CEST
    Description : 
    Usage       :

"""

from flask import make_response, jsonify

def error_response(status_code, message=None):
    # Return json error object.
    return make_response(jsonify({
        'status': 'fail',
        'message': message
    })), status_code


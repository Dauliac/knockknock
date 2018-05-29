#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:29:10 AM CEST
    Description : 
    Usage       :

"""

from flask import abort

def error_response(status_code, message=None):
    # Return json error object.
    abort(status_code)
    return { 'message': message }


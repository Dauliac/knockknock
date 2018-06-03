"""
    Author      : github.com/TonyChG
    Date        : Sat 02 Jun 2018 10:16:14 PM CEST
    Description : 
    Usage       :

"""

from flask import make_response, jsonify

def error_response(message, status_code):
    return make_response(jsonify({
        'status': 'fail',
        'message': message
        })), status_code


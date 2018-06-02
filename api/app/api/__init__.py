"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:12:28 AM CEST
    Description : 
    Usage       :

"""

from flask import Blueprint, render_template

api = Blueprint('api', __name__)

from app.api import users, ringtones, errors

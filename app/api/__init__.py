"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:12:28 AM CEST
    Description : 
    Usage       :

"""

from flask import Blueprint, render_template

api = Blueprint('api', __name__)

<<<<<<< HEAD
from app.api import users, ringtones, errors
=======
from app.api import users, auth, ringtones, errors

>>>>>>> 7a2c2df2ce31fd38219b06b0594a0675e6d2c7f7

#!/usr/bin/env python3.5
"""
    Author      : github.com/TonyChG
    Date        : Sat 02 Jun 2018 07:54:33 PM CEST
    Description : 
    Usage       :

"""

import os
import mysql.connector
from flask import g, current_app as app
from .models.User import User

def get_models():
    models = {}
    models['User'] = User()
    # models['Ringtones']

    return models

#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:30:54 AM CEST
    Description : 
    Usage       :

"""

from flask import Flask
import pymysql.cursors
from database import connector
import app.constants as cst

def configure():
    # Connect to DB
    db = Connection(cst.SQL_USER, cts.SQL_PWD, cst.SQL_HOST, cst.SQL_DB)
    db.connect()
    # Validate all api tokens
    # Validate models
    # Import configs
    pass

def init():
    # Bind routes
    from app.api import api

    app = Flask(__name__)
    # app.config.from_object('config')
    app.secret_key = "secret"
    app.register_blueprint(api, url_prefix='/api')

    return app


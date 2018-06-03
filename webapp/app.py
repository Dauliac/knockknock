#!/usr/bin/env python3.5
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:36:00 AM CEST
    Description : 
    Usage       :

"""

import os
import sys
import api
from api.users import bp as users
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from database import get_models
from flask_cors import CORS, cross_origin

def configure(app):
    app.config.from_object('config')
    os.environ['FLASK_ENV'] = 'production'

app = Flask(__name__)
cors = CORS(app, ressources={r"/api/*": {"origins": "*"}})
CORS(app)
app.register_blueprint(api.bp)
app.register_blueprint(users)
configure(app)

with app.app_context():
    try:
        models = get_models()
    except Exception as e:
        sys.stderr.write("Cannot established connection to mysql server.\n")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/createtestadm', methods=['GET'])
def createDefaultAdmin():
    user = { 'email': 'admin@example.com', 'password': 'password' }
    models = get_models()
    models['User'].create(user['email'], user['password'])
    return jsonify(user)

app.run(debug=True, host="0.0.0.0")


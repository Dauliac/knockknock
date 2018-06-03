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
from flask import Flask, render_template
from database import get_models

def configure(app):
    app.config.from_object('config')
    os.environ['FLASK_ENV'] = 'production'

app = Flask(__name__)
app.register_blueprint(api.bp)
configure(app)

with app.app_context():
    try:
        models = get_models()
        User = models['User']
        User.flush()
        User.create('admin@example.com', 'password')
    except Exception as e:
        sys.stderr.write("Cannot established connection to mysql server.\n")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

app.run(debug=True, host="0.0.0.0")


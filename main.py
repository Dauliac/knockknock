#!/usr/bin/python3
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:36:00 AM CEST
    Description : 
    Usage       :

"""

from app import configure, init
from flask_socketio import SocketIO

if __name__ == '__main__':
    app = init()
    socketio = SocketIO(app)
    socketio.run(app, host='0.0.0.0')

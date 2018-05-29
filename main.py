#!/usr/bin/python
# coding: utf-8
"""
    Author      : github.com/TonyChG
    Date        : Wed 16 May 2018 03:36:00 AM CEST
    Description : 
    Usage       :

"""

from app import configure, init
if __name__ == '__main__':
    app = init()
    app.run(debug=True, host='0.0.0.0')

"""
    Author      : github.com/TonyChG
    Date        : Sat 02 Jun 2018 04:21:53 PM CEST
    Description : 
    Usage       :

"""

import mysql.connector

def commit(client, querystring):
    cursor = client.cursor()
    cursor.execute(querystring)
    client.commit()

def results(client, querystring):
    cursor = client.cursor()
    cursor.execute(querystring)
    return cursor.fetchall()

def init_db(app):
    client = mysql.connector.connect(
            host=app.config["MYSQL_DATABASE_HOST"],
            user=app.config["MYSQL_DATABASE_USER"],
            password=app.config["MYSQL_DATABASE_PASSWORD"],
            database=app.config["MYSQL_DATABASE_DB"]
            )
    print(results(client, 'show tables'))
    return client

def get_models(client):
    return client

#!/usr/bin/python
from datetime import datetime, timedelta
from flask import Flask, url_for, render_template, request, redirect
import jwt
import pymysql.cursors

# Config

#   Flask
app = Flask(__name__)
app.debug = True

app.config.from_pyfile('config.py', silent=True)
app.config.from_pyfile('secret_config.py', silent=True)

#   Data base
connection = pymysql.connect(host=app.config.get('DB_HOST'),
                             user='DB_USER',
                             password='DB_PASSWORD',
                             db='DB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# Objects
class User(object):
    def __init__(self, id=None, username=None, password=None, admin=False):
        if id:
            self._id = id
        elif username and password:
            self._username = username
            self._password = password
            self._admin = admin
            self._insert()
        else:
            print('error empty user create one with new username and \
                   password or instance existing by id')

    def __str__(self):
        return "User(id='%s', username='%s', admin='%s' )" % (self._id, self._username, self._admin)

    def _insert(self):
        if self._username and self._password:
            try:
                with connection.cursor() as cursor:
                    insert_sql = "INSERT INTO `users` (`username`, `password`, `admin`)\
                                  VALUES (%s, %s, %s)"
                    cursor.execute(insert_sql,
                                   (self._username,
                                    self._password,
                                    self._admin))
                    get_sql = "SELECT username FROM users \
                               WHERE username='%s', password=''%s"
                    cursor.execute(get_sql, (self._username, self._password))
                    self._id = cursor.fetchone()
                connection.commit()
            finally:
                connection.close()

    @property
    def id(self, id):
        if self._id:
            return self._id
        try:
            with connection.cursor() as cursor:
                sql = "SELECT username FROM users WHERE user_id='%s'"
                cursor.execute(sql, self._id)
                self._username = cursor.fetchone()
                return self._username
        finally:
            connection.close()

    @property
    def username(self):
        if self._username:
            return self._username
        try:
            with connection.cursor() as cursor:
                sql = "SELECT username FROM users WHERE user_id='%s'"
                cursor.execute(sql, self.id)
                self._username = cursor.fetchone()
                return self._username
        finally:
            connection.close()

    @username.setter
    def set_username(self, username):
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE users SET username='%s' WHERE user_id='%s'"
                cursor.execute(sql, (username, self.id))
            connection.commit()
            self._username = username
        finally:
            connection.close()

    @property
    def password(self):
        if self._password:
            return self._password
        try:
            with connection.cursor() as cursor:
                sql = "SELECT password FROM users WHERE user_id='%s'"
                cursor.execute(sql, (self.id))
                self._password = cursor.fetchone()
                return self._password
        finally:
            connection.close()

    @password.setter
    def set_password(self, password):
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "UPDATE users SET password='%s' WHERE user_id='%s'"
                cursor.execute(sql, (password, self.id))
            connection.commit()
            self._password = password
        finally:
            connection.close()

    @property
    def admin(self): 
        if self._admin:
            return self._admin
        try:
            with connection.cursor() as cursor:
                sql = "SELECT admin FROM users WHERE user_id='%s'"
                cursor.execute(sql, self.id)
                self._admin = cursor.fetchone()
                return self._admin
        finally:
            connection.close()

    @admin.setter
    def set_admin(self, admin):
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "UPDATE USER SET admin='%s' WHERE user_id='%s'"
                cursor.execute(sql, (admin, self.id))
            connection.commit()
            self._admin = admin
        finally:
            connection.close()


# Functions
#   jwt

def encode_auth_token(self, user):
    """
    Generates the Auth Token
    return: string """
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, seconds=5),
            'iat': datetime.utcnow(),
            'sub': user.id,
            'name': user.username,
            'admin': user.admin
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    param auth_token:
    return: boolean|string
    """
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

def is_auth():
    token = request.cookies.get('token')
    if token:
        decode_auth_token(token)


# Routes
## Api

## Front-end
@app.route('/')
def index():
    if is_auth():
        return render_template('index.html')
    return redirect(url_for('login'))


@app.route('/login/')
def login():
    if is_auth():
        return redirect(url_for('index'))
    if request.method == 'POST':
        pass
    return render_template('login.html')


@app.route('/register/')
def register():
    return None


@app.route('/logout/')
def logout():
    return None


@app.route('/user/')
def user():
    return None




# Running 
if __name__ == '__main__':
    app.run()

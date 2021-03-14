from peewee import MySQLDatabase
from flask import Flask

DATABASE_NAME = 'SQ4Y6h3Ze5'
DATABASE_USERNAME = 'SQ4Y6h3Ze5'
DATABASE_PASSWORD = '7wW8rMNehQ'
DATABASE_PORT = 3306
DATABASE_HOST = 'remotemysql.com'

db = MySQLDatabase(
    DATABASE_NAME,
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)

app = Flask(__name__)


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


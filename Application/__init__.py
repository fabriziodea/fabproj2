from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nuovo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secretkey')

#'sqlite:///data.db'
#'sqlite:///nuovo.db'
#getenv('db_uri')
# remember to export db_uri e secretkey

db = SQLAlchemy(app)


import Application.models
import Application.forms
import Application.routes

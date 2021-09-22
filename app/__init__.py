# Importing Tokens
# from tkinter import *
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import backref
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thiscannotbeguessed'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitess.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes
#Importing Tokens........................
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import backref
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

#Initializing and Configuring App.......................
app = Flask(__name__)
app.config['SECRET_KEY'] = '3d2c4c8de6820c78ea3c607161cc0904205c950ba52f37d0a6869c2dc5899db2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitess.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.category = 'info'


from app import routes
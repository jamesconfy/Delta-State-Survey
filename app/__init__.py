# Importing Tokens........................
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager, login_manager
from config import Config

# Initializing and Configuring App.......................
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from users.routes import users
    from main.routes import main
    from lodgement.routes import lodgement

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(lodgement)

    with app.app_context():
        db.create_all()

    return app
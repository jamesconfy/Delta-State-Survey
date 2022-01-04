from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    prefix = db.Column(db.String(2), nullable=False)
    phone_no = db.Column(db.String(15), unique=True, nullable= False)
    location = db.Column(db.String(300))
    date_created = db.Column(db.DateTime(120), default=datetime.utcnow)
    image_file = db.Column(db.String(120), nullable=False, default='default.png')
    plans = db.relationship('Lodgement', backref='surveyor', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.prefix}')"

class Lodgement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_survey = db.Column(db.String(300), nullable=False)
    prefix = db.Column(db.String(2), nullable=False)
    plan_no = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(300), nullable=False)
    purpose_of_survey = db.Column(db.String(120), nullable=False)
    date_of_survey = db.Column(db.DateTime(120), default=datetime.utcnow)
    area_of_land = db.Column(db.Integer, nullable=False)
    lodegement_fee = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime(120), default=datetime.utcnow)
    plan_file = db.Column(db.String(120), nullable=False, default='default.png')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Lodgement('{self.name_of_survey}', '{self.plan_file}', '{self.prefix}')"
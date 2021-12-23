import os

class Config:
    #DB_USER = os.environs.get('SECRET_KEY')
    #DB_PASS = os.environs.get('SECRET_KEY')
    #SECRET_KEY = os.environs.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.environs.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = '3d2c4c8de6820c78ea3c607161cc0904205c950ba52f37d0a6869c2dc5899db2'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sitess.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

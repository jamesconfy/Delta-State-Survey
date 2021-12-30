import os

class Config:
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_HOST = os.environ.get('DB_HOST')

    SECRET_KEY = '3d2c4c8de6820c78ea3c607161cc0904205c950ba52f37d0a6869c2dc5899db2'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    use_native_code  = False
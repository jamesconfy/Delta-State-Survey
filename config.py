import os
from dotenv import load_dotenv

load_dotenv("app.env")

class Config:
    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_HOST = os.environ.get('DB_HOST')

    # print(DB_HOST, DB_PASS, DB_USER)

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/delta-survey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    use_native_code  = False
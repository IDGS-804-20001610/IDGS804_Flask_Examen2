from sqlalchemy import create_engine

import os
import urllib

class Config(object):
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/examen2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
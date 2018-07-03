import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'flask-rest')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_DB = 'dev'
    MONGO_HOST = 'mongodb://127.0.0.1:27017/dev'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGO_DB = 'testing'
    MONGO_HOST = 'mongodb://127.0.0.1:27017/testing'


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

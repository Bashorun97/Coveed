import os

basedir = os.getcwd()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('secret')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'coveed_dev.sqlite') or os.getenv('DEV_URI')
    DEBUG = True

class TestingConfig(Config):
    TESTING =True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'coveed-test.sqlite') or os.getenv('TEST_URI')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


config = {
    'development':DevelopmentConfig,
    'Testing':TestingConfig,
    'Production':ProductionConfig,

    'default':DevelopmentConfig
}


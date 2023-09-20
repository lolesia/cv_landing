import os

BASE_DIR = os.path.abspath(os.path.dirname("cv_landing"))


class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123123123@localhost:5432/cv_landing'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass




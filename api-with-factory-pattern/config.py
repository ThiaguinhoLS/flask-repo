# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):

    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"


class ProductionConfig(Config):

    DEBUG = False


# -*- coding: utf-8 -*-
import os.path

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "S3cr3t-k3y"

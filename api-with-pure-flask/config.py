# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(BASE_DIR, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


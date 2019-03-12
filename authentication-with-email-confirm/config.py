# -*- coding: utf-8 -*-
import os.path

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") \
        or "sqlite:///" + os.path.join(BASE_DIR, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "S3CR3T-K3Y"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SERVER = os.environ.get("MAIL_SERVER") or "smtp.gmail.com"
    MAIL_PORT = os.environ.get("MAIL_PORT") or 465
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") or False
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL") or True
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")


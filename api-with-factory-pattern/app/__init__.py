# -*- coding: utf-8 -*-
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from app.commands import test

db = SQLAlchemy()

def register_blueprints(app):

    "Register blueprints"

    from app.views import animals
    app.register_blueprint(animals)


def initialize_extensions(app):

    "Initialize all extensions"

    db.init_app(app)


def create_app(config_class=Config):

    "Factory app"

    app = Flask(__name__)
    app.config.from_object(config_class)
    initialize_extensions(app)
    register_blueprints(app)
    app.cli.add_command(test)
    with app.app_context():
        db.create_all()
    return app


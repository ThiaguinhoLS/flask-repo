# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app import commands

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.product.views import catalog
app.register_blueprint(catalog)
app.cli.add_command(commands.test)
db.create_all()


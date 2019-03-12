# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_login import login_required
from config import Config
from app.models import db, User, Link
from app.views import users, login_manager
from app.mail import mail

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(users)

    @app.shell_context_processor
    def make_shell_context():
        return { "db": db, "User": User, "Link": Link }

    @app.route("/")
    @login_required
    def index():
        return render_template("index.html")

    return app


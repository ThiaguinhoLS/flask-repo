# -*- coding: utf-8 -*-
from flask import Flask, render_template
from config import Config
from flask_login import login_required

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.views import login_manager, users
    from app.models import db

    # Initialize extensions
    login_manager.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(users)

    @app.route("/")
    @login_required
    def home():
        return render_template("home.html")

    return app


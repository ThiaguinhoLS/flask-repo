# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
import hashlib

db = SQLAlchemy()

class LinkHasExistError(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    is_activated = db.Column(db.Boolean, default=False, nullable=False)
    links = db.relationship("Link", backref="user", lazy=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.email = email

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_activate_link(self):
        if len(self.links) > 0:
            raise LinkHasExistError("Link has exist")
        self.links.append(Link(self.username))

    @property
    def link(self):
        return self.links[-1]

    def __repr__(self):
        return "<User: {}>".format(self.username)


class Link(db.Model):

    __tablename__ = "links"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, username, **kwargs):
        super(Link, self).__init__(**kwargs)
        self.generate_token(username)

    def generate_token(self, username):
        self.token = hashlib.md5(username.encode("utf-8")).hexdigest()


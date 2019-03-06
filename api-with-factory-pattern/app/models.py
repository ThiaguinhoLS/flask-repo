# -*- coding: utf-8 -*-
from app import db

class Animal(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Animal: {}>".format(self.name)


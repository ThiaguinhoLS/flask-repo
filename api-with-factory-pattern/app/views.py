# -*- coding: utf-8 -*-
from flask import Blueprint, abort, request, jsonify
from flask.views import MethodView
from app.models import Animal
from app import db

animals = Blueprint("animals", __name__, url_prefix="/animals")

class AnimalView(MethodView):

    def get(self, id=None):
        if not id:
            animals = Animal.query.all()
            res = {}
            for animal in animals:
                res[animal.id] = { "name": animal.name }
        else:
            animal = Animal.query.filter_by(id=id).first_or_404()
            res = { "name": animal.name }
        return jsonify(res)

    def post(self):
        name = request.form.get("name")
        if not name:
            abort(400)
        animal = Animal(name)
        db.session.add(animal)
        db.session.commit()
        return jsonify({ "name": animal.name }), 201

    def put(self, id):
        animal = Animal.query.filter_by(id=id).first_or_404()
        name = request.form.get("name")
        animal.name = name or animal.name
        db.session.commit()
        return jsonify({ "name": animal.name })

    def delete(self, id):
        animal = Animal.query.filter_by(id=id).first_or_404()
        db.session.delete(animal)
        db.session.commit()
        return "", 204


animal_view = AnimalView.as_view("animal_view")
animals.add_url_rule("/", view_func=animal_view, methods=["GET", "POST"])
animals.add_url_rule(
    "/<int:id>/",
    view_func=animal_view,
    methods=["GET", "PUT", "DELETE"]
)

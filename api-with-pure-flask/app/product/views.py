# -*- coding: utf-8 -*-
import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from app import app, db
from app.product.models import Product

catalog = Blueprint("catalog", __name__)

class ProductView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            products = Product.query.paginate(page, 10).items
            res = {}
            for product in products:
                res[product.id] = {
                    "name": product.name,
                    "price": str(product.price)
                }
        else:
            product = Product.query.filter_by(id=id).first()
            if not product:
                abort(404)
            res = {
                "name": product.name,
                "price": str(product.price)
            }
        return jsonify(res)

    def post(self):
        name = request.form.get("name")
        price = request.form.get("price")
        if not name or not price:
            abort(400)
        product = Product(name, price)
        db.session.add(product)
        db.session.commit()
        return jsonify({
            product.id: {
                "name": product.name,
                "price": str(product.price)
            }
        }), 201

    def put(self, id):
        product = Product.query.filter_by(id=id).first_or_404()
        name = request.form.get("name")
        price = request.form.get("price")
        product.name = name or product.name
        product.price = price or product.price
        db.session.commit()
        return jsonify({
            "name": product.name,
            "price": str(product.price)
        })

    def delete(self, id):
        product = Product.query.filter_by(id=id).first_or_404()
        db.session.delete(product)
        db.session.commit()
        return "", 204


product_view = ProductView.as_view("product_view")
app.add_url_rule("/product/", view_func=product_view, methods=["GET", "POST"])
app.add_url_rule(
    "/product/<int:id>/",
    view_func=product_view,
    methods=["GET", "PUT", "DELETE"]
)


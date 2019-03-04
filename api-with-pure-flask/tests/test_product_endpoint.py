# -*- coding: utf-8 -*-

import unittest
import os
from app import app, db
from config import Config, BASE_DIR
from app.product.models import Product

class ProductTestCase(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
            os.path.join(BASE_DIR, "test.db")
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        self.product = Product("abacate", 1.2)
        db.session.add(self.product)
        db.session.commit()

    def test_get_all_products(self):
        response = self.app.get("/product/")
        self.assertEqual(response.status_code, 200)

    def test_create_one_product(self):
        response = self.app.post("/product/", data={"name": "uva", "price": "1.2"})
        self.assertEqual(response.status_code, 201)

    def test_update_a_product(self):
        response = self.app.put("/product/{}/".format(self.product.id),
                                data={"name": "abacaxi"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "abacaxi")

    def test_delete_a_product(self):
        response = self.app.delete("/product/{}/".format(self.product.id))
        self.assertEqual(response.status_code, 204)


# -*- coding: utf-8 -*-
from app import create_app, db
from config import TestConfig
from unittest import TestCase
from app.models import Animal

class AnimalTestCase(TestCase):

    def setUp(self):
        app = create_app(TestConfig)
        self.app = app.test_client()
        self.animal = Animal("lion")
        ctx = app.app_context()
        ctx.push()
        db.session.add(self.animal)
        db.session.commit()

    def tearDown(self):
        db.drop_all()

    def test_get_all_animals(self):
        response = self.app.get("/animals/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Animal.query.all()), 1)
        self.assertEqual(len(response.get_json().items()), 1)

    def test_get_one_animal(self):
        response = self.app.get("/animals/{}/".format(self.animal.id))
        self.assertEqual(response.status_code, 200)

    def test_create_a_animal(self):
        response = self.app.post("/animals/", data={ "name": "monkey" })
        self.assertEqual(response.status_code, 201)

    def test_update_a_user(self):
        data = { "name": "bird" }
        response = self.app.put("/animals/{}/".format(self.animal.id), data=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_a_user(self):
        response = self.app.delete("/animals/{}/".format(self.animal.id))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Animal.query.all()), 0)


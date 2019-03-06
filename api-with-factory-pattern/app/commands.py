# -*- coding: utf-8 -*-
import click
import unittest
import os
from config import BASE_DIR

@click.command()
def test():

    "Tests with unittest"

    TEST_DIR = os.path.join(BASE_DIR, "tests")
    loader = unittest.TestLoader()
    suite = loader.discover(TEST_DIR)
    runner = unittest.TextTestRunner()
    runner.run(suite)


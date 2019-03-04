# -*- coding: utf-8 -*-
import click
import unittest
import os
from config import BASE_DIR

@click.command()
def test():

    "Tests with unittest"

    loader = unittest.TestLoader()
    TESTDIR = os.path.join(BASE_DIR, "tests")
    suite = loader.discover(TESTDIR)
    runner = unittest.TextTestRunner()
    runner.run(suite)


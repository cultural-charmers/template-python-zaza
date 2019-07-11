#!/usr/bin/env python3

"""Encapsulate {{ cookiecutter.charm_name_lc }} testing."""

import logging
import unittest

import zaza.model


class BasicTest(unittest.TestCase):
    """Encapsulate {{ cookiecutter.charm_name }} tests."""

    def test_{{ cookiecutter.charm_name_lc }}(self):
        logging.info('Testing {{ cookiecutter.charm_name_lc }}')

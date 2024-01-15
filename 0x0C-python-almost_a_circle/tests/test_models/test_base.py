#!/usr/bin/python3
""" will be the “test_base” """


from models.base import Base
import unittest


class test_base(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

#!/usr/bin/python3
""" Unittest for base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import path, remove


class Test_id(unittest.TestCase):
    """ Class for unittest of __init__ and id """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_no_arg(self):
        """ Id no argument """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_none(self):
        """ Id None """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base(None)
        self.assertEqual(b3.id, 3)

    def test_ints(self):
        """ Id int """
        b1 = Base(5)
        self.assertEqual(b1.id, 5)
        b2 = Base(-5)
        self.assertEqual(b2.id, -5)
        b3 = Base()
        self.assertEqual(b3.id, 1)

    def test_extra_args(self):
        """ More than 1 argument """
        with self.assertRaises(TypeError):
            b1 = Base(5, 1)

    def test_private(self):
        """ Check priv attribute in instance """
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects

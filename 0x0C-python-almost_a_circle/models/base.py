#!/usr/bin/python3
""" will be the “base” of all other classes"""


import json


class Base:
    """ will be the “base” of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            NewListDic = json.dumps(list_dictionaries)
            return NewListDic

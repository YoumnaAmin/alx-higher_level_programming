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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            NewListDic = json.dumps(list_dictionaries)
            return NewListDic

    @classmethod
    def save_to_file(cls, list_objs):
        jlist = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for i in list_objs:
                jlist.append(i.to_dictionary())
        list_objs_json = cls.to_json_string(jlist)
        
        with open(filename, "w", encoding="UTF8") as f:
            f.write(list_objs_json)

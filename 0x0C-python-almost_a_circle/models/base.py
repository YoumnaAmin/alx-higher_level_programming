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
        """to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            NewListDic = json.dumps(list_dictionaries)
            return NewListDic

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        jlist = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for i in list_objs:
                jlist.append(i.to_dictionary())
        list_objs_json = cls.to_json_string(jlist)

        with open(filename, "w", encoding="UTF8") as f:
            f.write(list_objs_json)

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        jlist2 = []
        if json_string is None or len(json_string) == 0:
            return jlist2
        jlist2 = json.loads(json_string)
        return jlist2

    @classmethod
    def create(cls, **dictionary):
        """to instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a file """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding="utf-8") as myfile:
                rd = myfile.read()
                dicst = cls.from_json_string(rd)
                inslist = []
                for i in dicst:
                    inslist.append(cls.create(**i))
                return inslist
        except IOError:
            return []

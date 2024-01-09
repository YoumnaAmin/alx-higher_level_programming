#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Geometry module"""
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """to validate int"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

"""Rectangle"""


class Rectangle(BaseGeometry):
    """constructor"""
    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

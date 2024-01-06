#!/usr/bin/python3
"""Rectangle dimensions"""


class Rectangle:
    """Rectangle dimensions"""
    def __init__(self, width=0, height=0):
        """Class constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """to calculate the area"""
        return self.__height * self.__width

    def perimeter(self):
        """to calculate the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """to print in str format"""
        char = ""
        if self.width == 0 or self.height == 0:
            return (char)
        else:
            for i in range(self.height):
                for j in range(self.width):
                    char += '#'
                if i != self.height - 1:
                    char += '\n'
        return char

    def __repr__(self):
        """ Method that returns Object Representation as string """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """to delete an object"""
        print("Bye rectangle... ")

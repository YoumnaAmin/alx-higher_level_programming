#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """to calculate the area"""
        return self.__height * self.__width

    def display(self):
        """to print in str format"""
        for k in range(self.y):
            print()
        char = ""
        if self.width == 0 or self.height == 0:
            print(char)
        else:
            for i in range(self.height):
                for e in range(self.x):
                    char += ' '
                for j in range(self.width):
                    char += '#'
                if i != self.height - 1:
                    char += '\n'
        print(char)

    def __str__(self):
        """to override the __str__"""
        return('[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'
               .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        if len(args) == 5:
            self.id, self.width, self.height, self.x, self.y = args[:]
        elif len(args) == 4:
            self.id, self.width, self.height, self.x = args[:4]
        elif len(args) == 3:
            self.id, self.width, self.height = args[:3]
        elif len(args) == 2:
            self.id, self.width = args[:2]
        elif len(args) == 1:
            self.id = args[0]

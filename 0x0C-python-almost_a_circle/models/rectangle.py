#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class respresenting rectangles
    it inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a rectangle object
        Args:
        width - width of the rectangle
        height - rectangle height
        x - x int cordinate of rectangle
        y - y int cordinate of rectangle
        id - rectangle identity
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/get width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return rectangle area"""
        return (self.__width * self.__height)

    def display(self):
        """prints a # rectangle considering x and y"""
        for _ in range(0, self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)
        if self.__width == 0 or self.height == 0:
            print("")

    def __str__(self):
        """"defines how a rectangle is represented"""
        return "[Rectangle] ({}) {}/{} - {}/{}" .format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height)

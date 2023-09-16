#!/usr/bin/python3
"""Rectangle Module that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle template"""
    def __init__(self, width, height):
        """Instantiation of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Defines how instances are represented"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns rectangle area"""
        return self.__width * self.__height

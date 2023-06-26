#!/usr/bin/python3
"""Square Module inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square template"""
    def __init__(self, size):
        """Instantiation of Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Defines square representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Returns square area"""
        return self.__size * self.__size

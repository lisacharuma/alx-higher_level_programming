#!/usr/bin/python3
""" defines Square"""


class Square:
    """Square rep"""

    def __init__(self, size=0):
        """Square initialization

        Arg:
        size(int): square size
        """
        self.size = size

    @property
    def size(self):
        """set & getsize"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints a # square"""
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")

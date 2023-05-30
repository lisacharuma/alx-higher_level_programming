#!/usr/bin/python3
""" defines Square"""


class Square:
    """Square rep"""

    def __init__(self, size=0, position=(0, 0)):
        """Square initialization

        Args:
        size(int): square size
        position(int, int): square cordinates
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """set & get position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value)
                or not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints a # square"""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")

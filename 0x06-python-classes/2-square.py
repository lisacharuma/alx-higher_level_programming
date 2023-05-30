#!/usr/bin/python3
"""Define Square class"""


class Square:
    """square representation"""

    def __init__(self, size=0):
        """new square initialization

        Arg:
        size(int): square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

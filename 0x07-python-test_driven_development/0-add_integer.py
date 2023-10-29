#!/usr/bin/python3
"""
This module has a function that adds two integers
"""


def add_integer(a, b=98):
    """
    Returns the sum of two numbers casted to integers

    Args:
    a: first argument
    b: second argument. If no arg is passed a default is used

    Raises:
    TypeError if either arg is not an int or float

    Return:
    Sum of two numbers in int
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

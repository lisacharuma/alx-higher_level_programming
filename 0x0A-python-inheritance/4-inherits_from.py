#!/usr/bin/python3
"""An object checking function"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a_class"""
    """Returns True if so otherwise False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class

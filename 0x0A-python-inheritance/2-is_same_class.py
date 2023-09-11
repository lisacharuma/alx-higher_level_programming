#!/usr/bin/python3
"""An object checking function"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class"""
    """If so it returns True else False"""
    return type(obj) is a_class

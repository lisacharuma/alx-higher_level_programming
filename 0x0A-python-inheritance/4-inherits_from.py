#!/usr/bin/python3
"""Defining an object checking function"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance  of a_class
    if so, it returns True
    else it returns False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class

#!/usr/bin/python3
"""Defining an object checking function"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance  of a_class
    if so, it returns True
    else it returns False"""
    return type(obj) is a_class

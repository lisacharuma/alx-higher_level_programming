#!/usr/bin/python3
"""Module defining add_attribute function"""


def add_attribute(obj, name, value):
    """A function that adds a new attr to an obj"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

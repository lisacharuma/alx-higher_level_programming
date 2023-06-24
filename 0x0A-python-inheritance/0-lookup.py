#!/usr/bin/python3
"""Defining a lookup function"""


def lookup(obj):
    """A function that returns a list of available attrs and
    methods of an object like the dir function"""
    attributes = [attr for attr in dir(obj) if not attr.startswith("__")]
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    return attributes + methods

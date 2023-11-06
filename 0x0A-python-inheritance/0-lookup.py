#!/usr/bin/python3
"""Defining a lookup function"""


def lookup(obj):
    """Returns a list of available attrs and methods of an obj
    using the dir function"""
    return dir(obj)

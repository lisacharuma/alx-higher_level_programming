#!/usr/bin/python3
"""Defining a lookup function"""


def lookup(obj):
    """A function that returns a list of available attrs and
    methods of an object using the dir function"""
    return dir(obj)

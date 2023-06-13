#!/usr/bin/python3
"""In this module a function that appends to a file is defined"""


def append_write(filename="", text=""):
    """A function that appends to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))

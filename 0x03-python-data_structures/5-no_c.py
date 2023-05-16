#!/usr/bin/python3
"""Removes characters C and c from given strings"""


def no_c(my_string):
    new_str = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(new_str))

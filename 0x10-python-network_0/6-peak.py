#!/usr/bin/python3
"""Find peak module"""


def find_peak(list_of_integers):
    """Returns peak number in a list"""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]

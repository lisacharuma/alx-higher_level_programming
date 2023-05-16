#!/usr/bin/python3
"""print a reversed list using the reverse function"""


def print_reversed_list_integer(my_list=[]):
    """check if my_list is a list"""
    if not isinstance(my_list, list):
        return
    new_list = my_list[::-1]
    for i in new_list:
        print("{:d}".format(i))

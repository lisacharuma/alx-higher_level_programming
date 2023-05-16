#!/usr/bin/python3
"""print a reversed list using the reverse function"""


def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    for i in new_list:
        print("{:d}".format(i))

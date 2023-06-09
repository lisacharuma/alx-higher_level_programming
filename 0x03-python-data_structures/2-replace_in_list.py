#!/usr/bin/python3
""" new_in_list - replaces an element in a list"""


def replace_in_list(my_list, idx, element):
    if not isinstance(my_list, list):
        return (my_list)
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    my_list[idx] = element
    return (my_list)

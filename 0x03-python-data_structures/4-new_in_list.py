#!/usr/bin/python3
"""new_in_list - replaces an element with the given one"""


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    new_list = [i for i in my_list]
    new_list[idx] = element
    return (new_list)

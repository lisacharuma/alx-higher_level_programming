#!/usr/bin/python3
"""Search and replace an element in list"""


def search_replace(my_list, search, replace):
    """
    Args:
    my_list - list where search and replace is performed
    search - value to be replaces
    replace - new value
    """
    new_list = my_list[:]
    list_len = len(new_list)

    for i in range(list_len):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)

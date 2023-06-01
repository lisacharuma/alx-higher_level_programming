#!/usr/bin/python3
"""Search and replace an element in list"""


def search_replace(my_list, search, replace):
    """
    Args:
    my_list - list where search and replace is performed
    search - value to be replaces
    replace - new value
    """
    
    list_len = len(my_list)
    for i in range(list_len):
        if my_list[i] == search:
            my_list[i] = replace
    return (my_list)

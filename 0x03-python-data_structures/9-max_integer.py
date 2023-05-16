#!/usr/bin/python3
"""max_integer - returns maximum int in a list"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    """set max to first int"""
    highest = my_list[0]
    """loop thru list comparing with highest"""
    for i in range(len(my_list)):
        """if an item is > highest, make it the new highest"""
        if my_list[i] > highest:
            highest = my_list[i]
    return (highest)

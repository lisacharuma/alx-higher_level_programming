#!/usr/bin/python3
"""divisible_by - checks if an item is divisible by 2"""


def divisible_by_2(my_list=[]):
    """ blank list to store bool values"""
    mult_list = []
    """loop thru list, if item is divisible by 2 add True to list"""
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mult_list.append(True)
        else:
            mult_list.append(False)
    return (mult_list)

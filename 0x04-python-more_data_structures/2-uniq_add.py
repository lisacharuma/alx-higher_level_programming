#!/usr/bin/python3
"""adds unique integers"""


def uniq_add(my_list=[]):
    total = 0
    new_list = list(dict.fromkeys(my_list))
    for i in range(len(new_list)):
        total = total + new_list[i]
    return (total)

#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """A function that prints x elements of a list.

    Args:
        my_list (list): list with elements.
        x (int): Number of elements to b printed

    Returns:
        number of printed elements"""

    num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num += 1
        except IndexError:
            break
    print("")
    return (num)

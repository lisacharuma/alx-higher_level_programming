#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integer elements of a list

    Args:
        my_list (list): list with elements
        x (int): number of elements to be printed

    Returns:
        printed elements count
    """

    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)

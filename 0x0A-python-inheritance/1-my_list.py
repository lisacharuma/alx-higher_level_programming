#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList template"""
    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)

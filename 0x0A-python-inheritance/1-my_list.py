#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList template"""
    def print_sorted(self):
        """prints the list sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)

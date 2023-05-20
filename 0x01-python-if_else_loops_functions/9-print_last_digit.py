#!/usr/bin/python3
"""Prints a number's last digit and return it"""


def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)

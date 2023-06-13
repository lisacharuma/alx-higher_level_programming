#!/usr/bin/python3
""" The function in this module reads a text file and prints to stdout"""


def read_file(filename=""):
    """Reads and prints file contents"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

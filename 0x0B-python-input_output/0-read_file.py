#!/usr/bin/python3
""" The function in this module reads a text file and prints to stdout"""


def read_file(filename=""):
    """Reads and prints file contents"""
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text)

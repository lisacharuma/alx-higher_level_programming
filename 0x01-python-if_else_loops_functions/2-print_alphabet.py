#!/usr/bin/python3
"""Prints ASCII alphabet in lower case"""


char = ord('a')

while char <= ord('z'):
    print(chr(char), end="")
    char += 1

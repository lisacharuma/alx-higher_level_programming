#!/usr/bin/python3
"""Prints numbers in hexadecimal"""


num = 0
while num <= 98:
    hexnum = hex(num)
    print(f"{num} = {hexnum}")
    num += 1

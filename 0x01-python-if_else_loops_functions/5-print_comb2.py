#!/usr/bin/python3
"""prints 0 to 99"""


num = 0

while num <= 99:
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
    num += 1

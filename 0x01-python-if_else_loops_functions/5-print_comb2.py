#!/usr/bin/python3
"""prints 0 to 99"""


num = 0

while num <= 99:
    print("{:02d}".format(num), end="")
    if num != 99:
        print(", ", end="")
    else:
        print()
    num += 1
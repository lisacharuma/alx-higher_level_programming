#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res = abs(number) % 10
if number < 0:
    res = -res
if res == 0:
    print(f"Last digit of {number} is {res} and is 0")
elif res < 6 and res != 0:
    print(f"Last digit of {number} is {res} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {res} and is greater than 5")

#!/usr/bin/python3
char = ord('a')

while char <= ord('z'):
    if char != ord('e') and char != ord('q'):
        print("{}".format(chr(char)), end="")
    char += 1

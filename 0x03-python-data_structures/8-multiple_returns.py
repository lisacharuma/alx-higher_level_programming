#!/usr/bin/python3
"""multiple_returns - returns str len at first char"""


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])

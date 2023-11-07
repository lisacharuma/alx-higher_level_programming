#!/usr/bin/python3
"""Module defining a function writing an object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes to a text file using JSON"""
    with open(filename, "w") as fp:
        json.dump(my_obj, fp)

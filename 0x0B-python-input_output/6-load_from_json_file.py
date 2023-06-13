#!/usr/bin/python3
"""Module defines a function that creates an obj from a JSON file"""
import json


def load_from_json_file(filename):
    """A function that creates a Python obj frm a jsn file"""
    with open(filename) as fp:
        return (json.load(fp))

#!/usr/bin/python3
"""Module defining a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """This function returns an object represented by a JSON string"""
    return (json.loads(my_str))

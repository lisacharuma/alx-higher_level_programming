#!/usr/bin/python3
"""Base class module"""
import json


class Base:
    """ Base class
    This is a base class for this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialises a new base object
        Arg:
        id: the new base's identity
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

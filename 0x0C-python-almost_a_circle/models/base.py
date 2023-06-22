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

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves JSON string representation of list_obj to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        j_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as fp:
            fp.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """"returns a list of the JSON string rep of json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

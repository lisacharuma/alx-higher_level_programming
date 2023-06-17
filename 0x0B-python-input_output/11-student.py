#!/usr/bin/python3
"""class Student module"""


class Student:
    """Class representing a student"""
    def __init__(self, first_name, last_name, age):
        """New student obj initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a json rep of a student object
        All attrs must be retrieved execpt when attrs
        is a list of strings.
        """
        if attrs is None:
            return (self.__dict__)
        else:
            return {key: getattr(self, key) for key
                    in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """Replaces all atrributes of the student
        """
        for key, val in json.items:
            setattr(self, key, val)

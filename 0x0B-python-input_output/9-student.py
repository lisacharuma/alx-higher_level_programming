#!/usr/bin/python3
"""class Student module"""


class Student:
    """Class representing a student"""
    def __init__(self, first_name, last_name, age):
        """New student obj initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a json rep of a student object"""
        return (self.__dict__)

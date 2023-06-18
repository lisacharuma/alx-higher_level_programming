#!/usr/bin/python3
"""Base class module"""


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

#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """Base geometry template"""
    def area(self):
        """A function to calcualate area
        raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates passed values"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

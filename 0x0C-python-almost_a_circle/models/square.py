#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square
    It inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square object.
        Args:
            size (int): Square size (width/height)
            x (int): square x-coordinate
            y (int): square y-coordinate
            id (int): square id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size attribute getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """Size attribute setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string representation of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Updates Square attributes"""
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for attr, value in zip(attr_names, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dict representation of square"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
            }

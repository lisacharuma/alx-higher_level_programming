#!/usr/bin/python3
"""Base class module"""
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as fp:
                json_data = fp.read()
                if json_data:
                    dictionaries = cls.from_json_string(json_data)
                    instances = []
                    for dictionary in dictionaries:
                        instance = cls.create(**dictionary)
                        instances.append(instance)
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to CSV file format"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as fp:
            writer = csv.writer(fp)
            if list_objs is None or len(list_objs) == 0:
                writer.writerow([])
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                writer.writerow(fields)
                for obj in list_objs:
                    row = [getattr(obj, field) for field in fields]
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file"""
        filename = cls.__name__ + ".csv"
        objects = []
        try:
            with open(filename, mode='r') as fp:
                reader = csv.DictReader(fp)
                for row in reader:
                    c_dict = {field: int(row[field]) for field in row.keys()}
                    obj = cls.create(**c_dict)
                    objects.append(obj)
        except FileNotFoundError:
            return []
        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a new window and draws rectangle and squares"""
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.setup(800, 600)

        """creating a turtle object for drawing"""
        pen = turtle.Turtle()
        pen.speed(0)
        """draw rectangles"""
        pen.color("red")
        for rectangle in list_rectangles:
            width = rectangle.width
            height = rectangle.height
            pen.penup()
            pen.goto(0, 0)
            pen.pendown()
            pen.forward(width)
            pen.right(90)
            pen.forward(height)
            pen.right(90)
            pen.forward(width)
            pen.right(90)
            pen.forward(height)
            pen.right(90)

        """Squares"""
        pen.color("blue")
        for square in list_squares:
            size = square.size
            pen.penup()
            pen.goto(0, 0)
            pen.pendown()
            for _ in range(4):
                pen.forward(size)
                pen.right(90)
        turtle.done()

#!/usr/bin/python3
"""Rectangle test module"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init(self):
        # Case 1: Testing constructor
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_str(self):
        # Case 2: Testing __str__ method
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_width_getter_setter(self):
        # Case 3: Testing width getter and setter
        r = Rectangle(1, 2)
        r.width = 3
        self.assertEqual(r.width, 3)
        with self.assertRaises(ValueError):
            r.width = -1
        with self.assertRaises(TypeError):
            r.width = "not_an_integer"

    def test_height_getter_setter(self):
        # Case 4: Testing height getter and setter
        r = Rectangle(1, 2)
        r.height = 4
        self.assertEqual(r.height, 4)
        with self.assertRaises(ValueError):
            r.height = -1
        with self.assertRaises(TypeError):
            r.height = "not_an_integer"

    def test_x_getter_setter(self):
        # Case 5: x getter and setter
        r = Rectangle(1, 2)
        r.x = 3
        self.assertEqual(r.x, 3)
        with self.assertRaises(ValueError):
            r.x = -1
        with self.assertRaises(TypeError):
            r.x = "not_an_integer"

    def test_y_getter_setter(self):
        # Case 6: y getter and setter
        r = Rectangle(1, 2)
        r.y = 4
        self.assertEqual(r.y, 4)
        with self.assertRaises(ValueError):
            r.y = -1
        with self.assertRaises(TypeError):
            r.y = "not_an_integer"

    def test_area(self):
        # Case 7: area()
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        # Case 8: display()
        r = Rectangle(2, 2)
        r.display()

    def test_update(self):
        # Case 9: update()
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8, 9, 10)
        self.assertEqual(r.id, 6)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

    def test_to_dictionary(self):
        # Case 10: to_dictionary()
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

if __name__ == '__main__':
    unittest.main()

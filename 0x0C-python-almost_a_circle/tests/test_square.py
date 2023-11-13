#!/usr/bin/python3
"""Square testing module"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_init(self):
        # Case 1: constructor
        s = Square(3, 4, 5, 6)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)
        self.assertEqual(s.id, 6)

    def test_str(self):
        # Case 2: _str_()
        s = Square(3, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (6) 4/5 - 3")

    def test_size_getter_setter(self):
        # Case 3: size getter and setter
        s = Square(3)
        s.size = 4
        self.assertEqual(s.size, 4)
        with self.assertRaises(ValueError):
            s.size = -1
        with self.assertRaises(TypeError):
            s.size = "not_an_integer"

    def test_update(self):
        # Case 4: update()
        s = Square(3, 4, 5, 6)
        s.update(7, 8, 9, 10)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 9)
        self.assertEqual(s.y, 10)

    def test_to_dictionary(self):
        # Case 5: to_dictionary()
        s = Square(3, 4, 5, 6)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 6, 'size': 3, 'x': 4, 'y': 5})

if __name__ == '__main__':
    unittest.main()

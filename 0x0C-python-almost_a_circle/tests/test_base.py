#!/usr/bin/python3
"""Base class unit test"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Tests methods in Base"""
    #Case 1: _init_ method
    def test_init(self):
        obj = Base()
        self.assertEqual(obj.id, 1)  # initializes id to 1
        obj2 = Base(5)
        self.assertEqual(obj2.id, 5)  # Check if id is set correctly

    def test_to_json_string(self):
        #Case 2: test to_json_string method
        obj = Base()
        json_str = obj.to_json_string([{"key": "value"}])
        # Checks if JSON string is generated correctly
        self.assertEqual(json_str, '[{"key": "value"}]')

    def test_save_to_file(self):
        # Case 3: test save_to_file method
        obj = Base()
        obj.save_to_file([])

if __name__ == '__main__':
    unittest.main()

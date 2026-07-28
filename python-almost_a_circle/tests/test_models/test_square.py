#!/usr/bin/python3
"""Unittest module for models/square.py."""
import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        for f in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(f):
                os.remove(f)

    def test_instantiation(self):
        s1 = Square(5)
        s2 = Square(5, 1, 2, 12)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.id, 12)

    def test_type_errors(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "1")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 1, "2")

    def test_value_errors(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 1, -2)

    def test_str(self):
        s = Square(5, 1, 2, 12)
        self.assertEqual(str(s), "[Square] (12) 1/2 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), d)

    def test_update(self):
        s = Square(5)
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_create(self):
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s1), "[Square] (89) 2/3 - 1")

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_squares(self):
        s1 = Square(5, 1, 2, 1)
        Square.save_to_file([s1])
        output = Square.load_from_file()
        self.assertEqual(str(s1), str(output[0]))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unittest module for models/rectangle.py."""
import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instantiation(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10, 1, 2, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.id, 12)

    def test_type_errors(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "1")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 1, "2")

    def test_value_errors(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 1, -2)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_xy(self):
        r = Rectangle(2, 2, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r.to_dictionary(), d)

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create(self):
        r1 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r1), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_and_load_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(output[0]))
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == '__main__':
    unittest.main()

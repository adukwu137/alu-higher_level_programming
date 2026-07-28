#!/usr/bin/python3
"""
Unittest module for models/base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class functionality."""

    def setUp(self):
        """Reset private class attribute before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test auto assignment of id."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_auto_id_increment(self):
        """Test increment of id across instances."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test custom id assignment."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_custom_id_negative(self):
        """Test negative custom id."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_custom_id_zero(self):
        """Test custom id equal to 0."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_mixed_ids(self):
        """Test auto id after custom id."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)


if __name__ == '__main__':
    unittest.main()

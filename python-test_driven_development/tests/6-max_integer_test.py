#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for max_integer function"""

    def test_ordered_list(self):
        """Test max at end of list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test max in middle of list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test max at beginning of list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test list with single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test list of float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_ints_and_floats(self):
        """Test list containing both ints and floats"""
        self.assertEqual(max_integer([1.5, 3, 2.7]), 3)

    def test_string(self):
        """Test string input"""
        self.assertEqual(max_integer("Python"), 'y')

    def test_list_of_strings(self):
        """Test list of strings"""
        self.assertEqual(max_integer(["apple", "zebra", "banana"]), "zebra")

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_positive_and_negative(self):
        """Test list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 0, -2]), 5)


if __name__ == '__main__':
    unittest.main()

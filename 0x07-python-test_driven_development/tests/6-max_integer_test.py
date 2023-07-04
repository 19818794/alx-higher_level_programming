#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    TestMaxInteger class.
    """

    def test_none_arg(self):
        """
        checks if the function with the case of none is provided.
        """
        self.assertRaises(TypeError, max_integer, None)

    def test_list_of_no_args(self):
        """
        checks if the function can handle no args passed case.
        """
        self.assertIsNone(max_integer())

    def test_list_empty(self):
        """
        checks if the function can handle an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_positive_integer(self):
        """
        checks if the function can give the highest positive integer.
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([0]), 0)

    def test_negative_integer(self):
        """
        checks if the function can give the highest negative integer.
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_list_of_negative_positive_integer(self):
        """
        checks if the function can handle a list of both
        negative and positive integer.
        """
        self.assertEqual(max_integer([1, 0, -3, -2]), 1)

    def test_positive_float(self):
        """
        checks if the function can give the highest positive float.
        """
        self.assertEqual(max_integer([1.23, 2.34, 3.45]), 3.45)

    def test_negative_float(self):
        """
        checks if the function can give the highest negative float.
        """
        self.assertEqual(max_integer([-1.23, -2.34, -3.45]), -1.23)

    def test_list_of_negative_positive_float(self):
        """
        checks if the function can handle a list of both
        negative and positive floats.
        """
        self.assertEqual(max_integer([-1.23, 2.34, -3.45]), 2.34)

    def test_character(self):
        """
        checks if the function can give the highest string.
        """
        self.assertEqual(max_integer(['a', 'z', 'A', 'z']), 'z')

    def test_empty_character(self):
        """
        checks if the function can handle empty character.
        """
        self.assertEqual(max_integer(''), None)

    def test_string(self):
        """
        checks if the function can give the highest string.
        """
        self.assertEqual(max_integer(['Jory', 'ray', 'Hol']), 'ray')
        self.assertEqual(max_integer('holberton'), 't')

    def test_empty_string(self):
        """
        checks if the function can handle empty string.
        """
        self.assertEqual(max_integer(""), None)

    def test_list_with_wrong_type(self):
        """
        checks if the function with a list of wrong type is provided.
        """
        self.assertRaises(TypeError, max_integer, [0, 1, "Hol"])


if __name__ == "__main__":
    unittest.main()


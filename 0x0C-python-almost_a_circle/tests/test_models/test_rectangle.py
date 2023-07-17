#!/usr/bin/python3
"""
tests/test_models/test_rectangle is an unittests for Rectangle class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
    test Rectangle class.
    """

    def test_rectangle_cls_docstring(self):
        """
        checks docstring for Rectangle class.
        """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_rectangle_methods_docstring(self):
        """
        checks docstring for all Rectangle methods.
        """
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(Rectangle.y.__doc__)

    def test_inheritance(self):
        """
        checks for inheritance.
        """
        r0 = Rectangle(10, 20)
        self.assertTrue(isinstance(r0, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(isinstance(Rectangle, Base))

    def test_missing_argumets(self):
        """
        checks for missing or over arguments.
        """
        s1 = "__init__() missing 1 required positional argument: 'height'"
        s2 = "__init__() missing 2 required positional argument"
        s3 = "__init__() takes from 3 to 6 positional arguments but "
        with self.assertRaises(TypeError) as e:
            r00 = Rectangle(10)
        self.assertEqual(s1, str(e.exception))
        with self.assertRaises(TypeError) as e:
            r000 = Rectangle()
        self.assertEqual(s2 + "s: 'width' and 'height'", str(e.exception))
        with self.assertRaises(TypeError) as e:
            r0000 = Rectangle(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(s3 + "10 were given", str(e.exception))

    @classmethod
    def setUpClass(cls):
        """
        setup class method.
        Also checks validation type and value of instantiation.
        """
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10)
        cls.r3 = Rectangle(10, 2, 0, 0, 12)
        cls.r4 = Rectangle(5, 6, 7, 8)

    def test_rectangle_private_instance_initiation(self):
        """
        checks the Rectangle initiation.
        """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.width, 10)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r4.width, 5)
        self.assertEqual(self.r4.height, 6)
        self.assertEqual(self.r4.x, 7)
        self.assertEqual(self.r4.y, 8)
        self.assertEqual(self.r4.id, 3)

    def test_rectangle_private_instance_assigning(self):
        """
        checks if Rectangle private instance assigned correctly.
        """
        self.assertEqual(self.r3.width, 10)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r3.id, 12)

    def test_rectangle_methods(self):
        """
        checks methods exist in Rectangle class.
        """
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(hasattr(Rectangle, "y"))


if __name__ == '__main__':
    unittest.main()

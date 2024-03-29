#!/usr/bin/python3
"""
tests/test_models/test_square is an unittests for Square class.
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import io
import contextlib


class TestSquare(unittest.TestCase):
    """
    test Square class.
    """

    def test_square_cls_docstring(self):
        """
        checks docstring for Square class.
        """
        self.assertIsNotNone(Square.__doc__)

    def test_square_methods_docstring(self):
        """
        checks docstring for all Square methods.
        """
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(Square.__str__.__doc__)
        self.assertTrue(Square.size.__doc__)
        self.assertTrue(Square.size.__doc__)
        self.assertTrue(Square.update.__doc__)

    def test_square_inheritance(self):
        """
        checks for inheritance.
        """
        sq0 = Square(2, 1, 2, 3)
        self.assertTrue(isinstance(sq0, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(sq0, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_square_missing_argumets(self):
        """
        checks for missing or over arguments.
        """
        s1 = "__init__() missing 1 required positional argument: 'size'"
        s2 = "__init__() takes from 2 to 5 positional arguments but "
        with self.assertRaises(TypeError) as e:
            sq0 = Square()
        self.assertEqual(s1, str(e.exception))
        with self.assertRaises(TypeError) as e:
            sq00 = Square(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(s2 + "10 were given", str(e.exception))

    @classmethod
    def setUpClass(cls):
        """
        setup class method.
        Also checks validation type and value of instantiation.
        """
        cls.sq1 = Square(10, 2, 3, 4)
        cls.sq2 = Square(20)

    def test_square_public_instance_initiation(self):
        """
        checks the Square initiation.
        """
        self.assertEqual(self.sq1.size, 10)
        self.assertEqual(self.sq1.width, 10)
        self.assertEqual(self.sq1.height, 10)
        self.assertEqual(self.sq1.x, 2)
        self.assertEqual(self.sq1.y, 3)
        self.assertEqual(self.sq1.id, 4)

    def test_square_methods(self):
        """
        checks methods exist in Square class.
        """
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(hasattr(Square, "size"))
        self.assertTrue(hasattr(Square, "size"))
        self.assertTrue(hasattr(Square, "update"))

    def test_square_methods_attributes_inherted(self):
        """
        checks methods and attributes inhertted frOOm Rectangle and Base.
        """
        sq4 = Square(3)
        self.assertEqual(sq4.size, 3)
        self.assertEqual(sq4.width, 3)
        self.assertEqual(sq4.height, 3)
        self.assertEqual(sq4.area(), 9)
        sq4.update(4)
        self.assertEqual(sq4.id, 4)
        sq4.update(y=2, x=2)
        self.assertEqual(sq4.x, 2)
        self.assertEqual(sq4.y, 2)
        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            sq4.display()
        s0 = str_io.getvalue()
        output = "\n\n  ###\n  ###\n  ###\n"
        self.assertEqual(s0, output)

    def test_square_validation_arguments(self):
        """
        checks validation arguments for Square class.
        """
        s0 = "validation() missing 2 required positional arguments: "
        with self.assertRaises(TypeError) as e:
            sq3 = Square(2, 3)
            sq3.validation()
            self.assertEqual(s0 + "'name' and 'value'", str(e.exception))
        s1 = "validation() missing 1 required positional argument: 'value'"
        with self.assertRaises(TypeError) as e:
            sq3.validation("width")
            self.assertEqual(s1, str(e.exception))
        s2 = "validation() takes 3 positional arguments but 9 were given"
        with self.assertRaises(TypeError) as e:
            sq3.validation("foo", 1, 2, 3, 4, 5, 6, 7)
            self.assertEqual(s2, str(e.exception))

    def test_square_validation_integer_type(self):
        """
        checks square if it inherts validation function frOOm Reactangle.
        """
        with self.assertRaises(TypeError):
            self.sq1.size = "foo"
            self.sq1.validation("size", "foo")
            self.sq1.height = "2"
            self.sq1.validation("height", "2")
            self.sq1.width = "hello"
            self.sq1.validation("width", "hello")
            self.sq1.x = "world"
            self.sq1.validation("x", "world")
            self.sq1.y = "2"
            self.sq1.validation("y", "2")
        with self.assertRaises(TypeError) as e:
            sq5 = Square("foo")
            self.assertEqual("width must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            sq6 = Square(10, "foo")
            self.assertEqual("x must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            sq7 = Square(10, 2, "foo")
            self.assertEqual("y must be an integer", str(e.exception))

    def test_validation_integer_value(self):
        """
        checks validation value of all setter methods.
        """
        with self.assertRaises(ValueError) as e:
            sq9 = Square(0, 2)
            self.assertEqual("width must be > 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            sq10 = Square(10, -1)
            self.assertEqual("x must be >= 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            r11 = Square(1, 2, -1)
            self.assertEqual("y must be >= 0", str(e.exception))

    def test_square_str_arguments(self):
        """
        check __str__ arguments.
        """
        s0 = "__str__() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            self.sq1.__str__("foo")
            self.assertEqual(s0, str(e.exception))

    def test_str(self):
        """
        checks __str__ representation value.
        """
        self.assertEqual(self.sq2.__str__(), "[Square] (1) 0/0 - 20")

    def test_size_attribute_wrong_type_value(self):
        """
        checks size attribute for wrong type or value.
        """
        with self.assertRaises(TypeError) as e:
            sq3 = Square("foo")
        self.assertEqual("width must be an integer", str(e.exception))
        with self.assertRaises(ValueError) as e:
            sq3 = Square(0)
        self.assertEqual("width must be > 0", str(e.exception))

    def test_update_effect_arguments(self):
        """
        checks update effect and arguments.****
        """
        self.assertEqual(self.sq1.__str__(), "[Square] (4) 2/3 - 10")
        self.sq1.update()
        self.assertEqual(self.sq1.__str__(), "[Square] (4) 2/3 - 10")
        self.sq1.update(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(self.sq1.__str__(), "[Square] (1) 3/4 - 10")
        self.sq1.update(11, 22, 33, 44)
        self.assertEqual(self.sq1.__str__(), "[Square] (11) 33/44 - 10")
        self.assertEqual(self.sq1.id, 11)
        self.assertEqual(self.sq1.size, 10)
        self.assertEqual(self.sq1.width, 10)
        self.assertEqual(self.sq1.height, 10)
        self.assertEqual(self.sq1.x, 33)
        self.assertEqual(self.sq1.y, 44)

    def test_update_wrong_arguments(self):
        """
        checks update with wrong arguments.
        """
        with self.assertRaises(TypeError) as e:
            self.sq2.update("foo")
            self.assertEqual("id must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.sq2.update(1, "foo")
            self.assertEqual("width must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.sq2.update(1, 2, "foo")
            self.assertEqual("x must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.sq2.update(1, 2, 3, "foo")
            self.assertEqual("y must be an integer", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.sq2.update(1, 0)
            self.assertEqual("width must be > 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.sq2.update(1, 2, -1)
            self.assertEqual("x must be >= 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.sq2.update(1, 2, 3, -4)
            self.assertEqual("y must be >= 0", str(e.exception))

    def test_update_kwargs(self):
        """
        checks update with kwargs.****
        """
        self.sq2.update(width=2)
        self.assertEqual(self.sq2.width, 20)
        self.assertEqual(self.sq2.height, 20)
        self.sq2.update(x=3)
        self.assertEqual(self.sq2.x, 3)
        self.sq2.update(y=5)
        self.assertEqual(self.sq2.y, 5)
        self.sq2.update(id=4)
        self.assertEqual(self.sq2.id, 4)
        self.sq2.update(y=2, x=4, id=1, width=5)
        self.assertEqual(self.sq2.id, 1)
        self.assertEqual(self.sq2.width, 20)
        self.assertEqual(self.sq2.height, 20)
        self.assertEqual(self.sq2.x, 4)
        self.assertEqual(self.sq2.y, 2)

    def test_update_kwargs_wrong_arguments(self):
        """
        checks update with wrong arguments in kwargs.
        """
        with self.assertRaises(TypeError) as e:
            self.sq2.update(width="foo")
        self.assertEqual("width must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.sq2.update(height="foo")
        self.assertEqual("height must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.sq2.update(x="foo")
        self.assertEqual("x must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.sq2.update(y="foo")
        self.assertEqual("y must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.sq2.update(id="foo")
        self.assertEqual("id must be an integer", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.sq2.update(width=0)
        self.assertEqual("width must be > 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.sq2.update(height=0)
        self.assertEqual("height must be > 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.sq2.update(x=-1)
        self.assertEqual("x must be >= 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.sq2.update(y=-1)
        self.assertEqual("y must be >= 0", str(e.exception))


if __name__ == '__main__':
    unittest.main()

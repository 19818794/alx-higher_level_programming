#!/usr/bin/python3
"""
tests/test_models/test_rectangle is an unittests for Rectangle class.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import contextlib


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
        self.assertTrue(Rectangle.validation.__doc__)
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(Rectangle.update.__doc__)

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
        cls.r18 = Rectangle(10, 2)
        cls.r19 = Rectangle(2, 3)

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
        self.assertTrue(hasattr(Rectangle, "validation"))
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(hasattr(Rectangle, "update"))

    def test_validation_arguments(self):
        """
        checks validation arguments.
        """
        s0 = "validation() missing 2 required positional arguments: "
        with self.assertRaises(TypeError) as e:
            r17 = Rectangle(2, 3)
            r17.validation()
            self.assertEqual(s0 + "'name' and 'value'", str(e.exception))
        s1 = "validation() missing 1 required positional argument: 'value'"
        with self.assertRaises(TypeError) as e:
            r17.validation("width")
            self.assertEqual(s1, str(e.exception))
        s2 = "validation() takes 3 positional arguments but 9 were given"
        with self.assertRaises(TypeError) as e:
            r17.validation("foo", 1, 2, 3, 4, 5, 6, 7)
            self.assertEqual(s2, str(e.exception))

    def test_validation_integer_type(self):
        """
        checks validation type of all setter methods.
        """
        with self.assertRaises(TypeError):
            self.r1.height = "2"
            self.r1.validation("2", "2")
            self.r2.width = "hello"
            self.r2.validation("hello", "hello")
            self.r3.x = "world"
            self.r3.validation("world", "world")
            self.r4.y = "2"
            self.r4.validation("2", "2")
        with self.assertRaises(TypeError) as e:
            r5 = Rectangle("hello", 2)
            self.assertEqual("width must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            r6 = Rectangle(10, "hello")
            self.assertEqual("height must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            r7 = Rectangle(10, 2, "hello")
            self.assertEqual("x must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            r8 = Rectangle(10, 2, 0, "hello")
            self.assertEqual("y must be an integer", str(e.exception))

    def test_validation_integer_value(self):
        """
        checks validation value of all setter methods.
        """
        r9 = Rectangle(1, 2)
        r10 = Rectangle(2, 3)
        r11 = Rectangle(4, 5)
        r12 = Rectangle(6, 7)
        with self.assertRaises(ValueError):
            r9.height = 0
            r9.validation(0, 0)
            r10.width = 0
            r10.validation(0, 0)
            r11.x = -1
            r11.validation(-1, -1)
            r12.y = -1
            r12.validation(-1, -1)
        with self.assertRaises(ValueError) as e:
            r13 = Rectangle(0, 2)
            self.assertEqual("width must be > 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            r14 = Rectangle(10, 0)
            self.assertEqual("height must be > 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            r15 = Rectangle(1, 2, -1)
            self.assertEqual("x must be >= 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            r16 = Rectangle(1, 2, 0, -1)
            self.assertEqual("y must be >= 0", str(e.exception))

    def test_area(self):
        """
        checks area value and arguments.
        """
        self.assertEqual(self.r18.area(), 20)
        s0 = "area() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            self.r18.area("foo")
            self.assertEqual(s0, str(e.exception))

    def test_display_argumets(self):
        """
        checks display arguments.
        """
        s0 = "display() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            self.r18.display("foo")
            self.assertEqual(s0, str(e.exception))

    def test_display(self):
        """
        checks display value.
        """
        str_io = io.StringIO()
        with contextlib.redirect_stdout(str_io):
            self.r18.display()
        s0 = str_io.getvalue()
        output = "##########\n##########\n"
        self.assertEqual(s0, output)

    def test_str_arguments(self):
        """
        check __str__ arguments.
        """
        s0 = "__str__() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            self.r18.__str__("foo")
            self.assertEqual(s0, str(e.exception))

    def test_str(self):
        """
        checks __str__ representation value.
        """
        self.assertEqual(self.r18.__str__(), "[Rectangle] (4) 0/0 - 10/2")

    def test_display_with_x_y(self):
        """
        checks display value by taking care of x and y.
        """
        str_io = io.StringIO()
        self.r19.x = 2
        self.r19.y = 3
        with contextlib.redirect_stdout(str_io):
            self.r19.display()
        s0 = str_io.getvalue()
        output = "\n\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s0, output)

    def test_update_effect_arguments(self):
        """
        checks update effect and arguments.
        """
        self.assertEqual(self.r19.__str__(), "[Rectangle] (5) 2/3 - 2/3")
        self.r19.update()
        self.assertEqual(self.r19.__str__(), "[Rectangle] (5) 2/3 - 2/3")
        self.r19.update(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(self.r19.__str__(), "[Rectangle] (1) 4/5 - 2/3")
        self.r19.update(11, 22, 33, 44, 55)
        self.assertEqual(self.r19.__str__(), "[Rectangle] (11) 44/55 - 22/33")
        self.assertEqual(self.r19.id, 11)
        self.assertEqual(self.r19.width, 22)
        self.assertEqual(self.r19.height, 33)
        self.assertEqual(self.r19.x, 44)
        self.assertEqual(self.r19.y, 55)

    def test_update_wrong_arguments(self):
        """
        checks update with wrong arguments.
        """
        with self.assertRaises(TypeError) as e:
            self.r19.update("foo")
            self.assertEqual("id must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.r19.update(1, "foo")
            self.assertEqual("width must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.r19.update(1, 2, "foo")
            self.assertEqual("height must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.r19.update(1, 2, 3, "foo")
            self.assertEqual("x must be an integer", str(e.exception))
        with self.assertRaises(TypeError) as e:
            self.r19.update(1, 2, 3, 4, "foo")
            self.assertEqual("y must be an integer", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.r19.update(1, 0)
            self.assertEqual("width must be > 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.r19.update(1, 2, 0)
            self.assertEqual("height must be > 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.r19.update(1, 2, 3, -4)
            self.assertEqual("x must be >= 0", str(e.exception))
        with self.assertRaises(ValueError) as e:
            self.r19.update(1, 2, 3, 4, -4)
            self.assertEqual("y must be >= 0", str(e.exception))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
tests/test_models/test_base is an unittests for Base class.
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    test Base class.
    """

    def test_base_cls_docstring(self):
        """
        checks docstring for Base class.
        """
        self.assertIsNotNone(Base.__doc__)

    def test_base_methods_docstring(self):
        """
        checks docstring for all Base methods.
        """
        self.assertTrue(Base.__init__.__doc__)

    def test_base_nbobjects_existance(self):
        """
        checks private class attribut if it has a value after initialisation.
        """
        self.assertIsNotNone(Base._Base__nb_objects)

    @classmethod
    def setUpClass(cls):
        """
        setup class method.
        """
        cls.b1 = Base()
        cls.b2 = Base(20)
        cls.b3 = Base()

    @classmethod
    def clear_objects(cls):
        """
        clears objects after tests.
        """
        del cls.b1
        del cls.b2
        del cls.b3

    def test_base_id_initiation(self):
        """
        checks the Base initiation.
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 20)
        self.assertEqual(self.b3.id, 2)

    def test_base_id_assigning(self):
        """
        checks if Base class public instance assigned correctly.
        """
        self.assertEqual(self.b1.id, 1)

    def test_base_id_incrementing(self):
        """
        checks object id if it is incrementing correctly.
        """
        self.assertIsNotNone(self.b1.id)
        self.assertIsNotNone(Base._Base__nb_objects)

    def test_base_methods(self):
        """
        checks methods exist in Base class.
        """
        self.assertTrue(hasattr(Base, "__init__"))


if __name__ == '__main__':
    unittest.main()

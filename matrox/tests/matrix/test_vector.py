import unittest

from matrox import *

class TestVectorOperations(unittest.TestCase):

    def test_repr(self):
        vector = Vector([1, 2, 3])
        self.assertEqual(repr(vector),
            "Vector(['1', '2', '3'])")

    def test_getitem(self):
        vector = Vector([1, 2, 3])
        self.assertEqual(repr(vector[0]), '1')

    def test_setitem(self):
        vector = Vector([1, 2, 3])
        self.assertEqual(repr(vector[0]), '1')
        vector[0] = 4
        self.assertEqual(repr(vector[0]), '4')

    def test_fraction(self):
        vector = Vector([1, 2, 3], fraction=True)
        self.assertEqual(repr(vector),
            "Vector(['1', '2', '3'])")

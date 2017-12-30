import unittest

from matrox import *

class TestVectorOperations(unittest.TestCase):

    def test_repr(self):
        vector = Vector([1, 2, 3])
        self.assertEqual(repr(vector),
            "Vector(['1', '2', '3'])")

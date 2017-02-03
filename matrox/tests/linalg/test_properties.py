import unittest

from matrox import (
    is_identity,
    fill_matrix,
    Matrix
)

from matrox.linalg import *

class TestProperties(unittest.TestCase):

    def test_rank(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]], fraction=True)
        matrix_rank = rank(matrix)
        self.assertEqual(repr(matrix_rank), "2")

        matrix = fill_matrix(3, 3, 2)
        matrix_rank = rank(matrix)
        self.assertEqual(repr(matrix_rank), "1")

    def test_inverse(self):
        matrix = Matrix([[1, 2], [3, 4]], fraction=True)
        inverted = inverse(matrix)
        self.assertEqual(repr(inverted),
            "Matrix([['-2', '1'], ['3/2', '-1/2']])")
        self.assertEqual(repr(is_identity(matrix * inverted)), "True")

        matrix = Matrix([[1, 1], [2, 2]], fraction=True)
        inverted = inverse(matrix)
        self.assertEqual(repr(inverted), "None")

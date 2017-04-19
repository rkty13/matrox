import unittest

from matrox import Matrix, fill_matrix
from matrox.linalg import *

class TestSpaces(unittest.TestCase):

    def test_null_basis(self):
        matrix_a = Matrix([[0, 2, 0, 0], 
                            [3, -1, 0, 0],
                            [0, 0, 0, 5], 
                            [0, 0, 0, 0]], fraction=True)
        self.assertEqual(repr(null_basis(matrix_a)),
            "[Matrix([['0'], ['0'], ['1'], ['0']])]")
 
    def test_back_substitution(self):
        U = Matrix([[1, 1, 2, 3], [0, 0, 4, 4], [0, 0, 0, 0]], fraction=True)
        x = Matrix([[0], [1], [0], [0]], fraction=True)
        b = Matrix([[0], [0], [0]], fraction=True)
        x_n = back_substitution(U, x, b)
        self.assertEqual(repr(x_n), "Matrix([['-1'], ['1'], ['0'], ['0']])")

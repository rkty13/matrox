import unittest

from matrox import Matrix, Vector, identity_matrix
from matrox.linalg import *

class TestSpaces(unittest.TestCase):

    def test_row_space(self):
        U = Matrix([[1, 3, 2],
                    [2, 7, 4],
                    [1, 5, 2]], fraction=True)
        self.assertEqual(repr(row_space(U)),
            "[Vector(['1', '0', '2']), Vector(['0', '1', '0'])]")

    def test_column_space(self):
        U = Matrix([[1, 3, 2],
                    [2, 7, 4],
                    [1, 5, 2]], fraction=True)
        self.assertEqual(repr(column_space(U)),
            "[Vector(['1', '2', '1']), Vector(['3', '7', '5'])]")

    def test_null_basis(self):
        matrix_a = Matrix([[0, 2, 0, 0], 
                            [3, -1, 0, 0],
                            [0, 0, 0, 5], 
                            [0, 0, 0, 0]], fraction=True)
        self.assertEqual(repr(null_basis(matrix_a)),
            "[Matrix([['0'], ['0'], ['1'], ['0']])]")
        matrix_b = identity_matrix(3)
        self.assertEqual(repr(null_basis(matrix_b)), "[]")
 
    def test_back_substitution(self):
        U = Matrix([[1, 1, 2, 3], [0, 0, 4, 4], [0, 0, 0, 0]], fraction=True)
        x = Matrix([[0], [1], [0], [0]], fraction=True)
        b = Matrix([[0], [0], [0]], fraction=True)
        x_n = back_substitution(U, x, b)
        self.assertEqual(repr(x_n), "Matrix([['-1'], ['1'], ['0'], ['0']])")

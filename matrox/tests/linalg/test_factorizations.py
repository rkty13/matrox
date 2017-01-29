import unittest

from matrox import Matrix, DimensionError
from matrox.linalg import *

class TestMatrixFactorizations(unittest.TestCase):

    def test_permute_matrix(self):
        matrix = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        permute = permute_matrix(matrix)
        self.assertEqual(repr(permute),
            "Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])")

        matrix = Matrix([[0, 1, 1], [1, 2, 1], [2, 7, 9]])
        permute = permute_matrix(matrix)
        self.assertEqual(repr(permute), 
            "Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])")

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            permute = permute_matrix(matrix)

        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

    def test_upper_triangular(self):
        matrix = Matrix([[2, 1], [6, 8]])
        upper, history, inverse_history = \
            upper_triangular(matrix, history=True, inverse_history=True)
        self.assertEqual(repr(upper), "Matrix([[2, 1], [0.0, 5.0]])")
        self.assertEqual(repr(history), "[Matrix([[1, 0], [-3.0, 1]])]")
        self.assertEqual(repr(inverse_history), "[Matrix([[1, 0], [3.0, 1]])]")

    def test_lower_triangular(self):
        matrix = Matrix([[2, 1], [6, 8]])
        lower, history, inverse_history = \
            lower_triangular(matrix, history=True, inverse_history=True)
        self.assertEqual(repr(lower), "Matrix([[1.25, 0.0], [6, 8]])")
        self.assertEqual(repr(history), "[Matrix([[1, -0.125], [0, 1]])]")
        self.assertEqual(repr(inverse_history), 
            "[Matrix([[1, 0.125], [0, 1]])]")

    def test_lu_factorization(self):
        matrix = Matrix([[2, 1], [6, 8]])
        lower, upper = lu_factorization(matrix)
        self.assertEqual(repr(lower), "Matrix([[1.0, 0], [3.0, 1]])")
        self.assertEqual(repr(upper), "Matrix([[2, 1], [0.0, 5.0]])")

    def test_ldu_factorization(self):
        pass

    def test_plu_factorization(self):
        pass

    def test_ldlt_factorization(self):
        pass

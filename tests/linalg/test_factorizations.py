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
        pass

    def test_lower_triangular(self):
        pass

    def test_lu_factorization(self):
        pass

    def test_ldu_factorization(self):
        pass

    def test_plu_factorization(self):
        pass

    def test_ldlt_factorization(self):
        pass

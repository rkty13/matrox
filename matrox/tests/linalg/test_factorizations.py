import unittest

from matrox import Matrix, DimensionError
from matrox.linalg import *

class TestMatrixFactorizations(unittest.TestCase):

    def test_permute_matrix(self):
        matrix = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        permute = permute_matrix(matrix)
        self.assertEqual(repr(permute),
            "Matrix([['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']])")

        matrix = Matrix([[0, 1, 1], [1, 2, 1], [2, 7, 9]])
        permute = permute_matrix(matrix)
        self.assertEqual(repr(permute),
            "Matrix([['0', '1', '0'], ['1', '0', '0'], ['0', '0', '1']])")

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            permute = permute_matrix(matrix)

        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

    def test_upper_triangular(self):
        matrix = Matrix([[2, 1], [6, 8]], fraction=True)
        upper, history, inverse_history = \
            upper_triangular(matrix, history=True, inverse_history=True)
        self.assertEqual(repr(upper), "Matrix([['2', '1'], ['0', '5']])")
        self.assertEqual(repr(history), "[Matrix([['1', '0'], ['-3', '1']])]")
        self.assertEqual(repr(inverse_history),
            "[Matrix([['1', '0'], ['3', '1']])]")

    def test_lower_triangular(self):
        matrix = Matrix([[2, 1], [6, 8]], fraction=True)
        lower, history, inverse_history = \
            lower_triangular(matrix, history=True, inverse_history=True)
        self.assertEqual(repr(lower), "Matrix([['5/4', '0'], ['6', '8']])")
        self.assertEqual(repr(history), "[Matrix([['1', '-1/8'], ['0', '1']])]")
        self.assertEqual(repr(inverse_history), 
            "[Matrix([['1', '1/8'], ['0', '1']])]")

    def test_lu_factorization(self):
        matrix = Matrix([[2, 1], [6, 8]], fraction=True)
        lower, upper = lu_factorization(matrix)
        self.assertEqual(repr(lower), "Matrix([['1', '0'], ['3', '1']])")
        self.assertEqual(repr(upper), "Matrix([['2', '1'], ['0', '5']])")
        self.assertEqual(repr(lower * upper), repr(matrix))

    def test_ldu_factorization(self):
        matrix = Matrix([[1, 5, 4], [3, 6, 4], [8, 2, 3]], fraction=True)
        lower, diag, upper = ldu_factorization(matrix)
        self.assertEqual(repr(lower),
            "Matrix([['1', '0', '0'], ['3', '1', '0'], ['8', '38/9', '1']])")
        self.assertEqual(repr(diag),
            "Matrix([['1', '0', '0'], ['0', '-9', '0'], ['0', '0', '43/9']])")
        self.assertEqual(repr(upper),
            "Matrix([['1', '5', '4'], ['0', '1', '8/9'], ['0', '0', '1']])")
        self.assertEqual(repr(lower * diag * upper), repr(matrix))

    def test_plu_factorization(self):
        matrix = Matrix([[1, 5, 4], [3, 6, 4], [8, 2, 3]], fraction=True)
        permuted, lower, upper = plu_factorization(matrix)
        self.assertEqual(repr(permuted),
            "Matrix([['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']])")
        self.assertEqual(repr(lower),
            "Matrix([['1', '0', '0'], ['3', '1', '0'], ['8', '38/9', '1']])")
        self.assertEqual(repr(upper),
            "Matrix([['1', '5', '4'], ['0', '-9', '-8'], ['0', '0', '43/9']])")

        matrix = Matrix([[0, 5, 4], [3, 0, 4], [8, 2, 3]], fraction=True)
        permuted, lower, upper = plu_factorization(matrix)
        self.assertEqual(repr(permuted),
            "Matrix([['0', '1', '0'], ['1', '0', '0'], ['0', '0', '1']])")
        self.assertEqual(repr(lower),
            "Matrix([['1', '0', '0'], ['0', '1', '0'], ['8/3', '2/5', '1']])")
        self.assertEqual(repr(upper),
            "Matrix([['3', '0', '4'], ['0', '5', '4'], ['0', '0', '-139/15']])")

    def test_ldlt_factorization(self):
        pass

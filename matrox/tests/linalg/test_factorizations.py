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

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            upper = upper_triangular(matrix)
        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

    def test_lower_triangular(self):
        matrix = Matrix([[2, 1], [6, 8]], fraction=True)
        lower, history, inverse_history = \
            lower_triangular(matrix, history=True, inverse_history=True)
        self.assertEqual(repr(lower), "Matrix([['5/4', '0'], ['6', '8']])")
        self.assertEqual(repr(history), "[Matrix([['1', '-1/8'], ['0', '1']])]")
        self.assertEqual(repr(inverse_history), 
            "[Matrix([['1', '1/8'], ['0', '1']])]")

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            lower = lower_triangular(matrix)
        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

    def test_lu_factorization(self):
        matrix = Matrix([[2, 1], [6, 8]], fraction=True)
        lower, upper = lu_factorization(matrix)
        self.assertEqual(repr(lower), "Matrix([['1', '0'], ['3', '1']])")
        self.assertEqual(repr(upper), "Matrix([['2', '1'], ['0', '5']])")
        self.assertEqual(repr(lower * upper), repr(matrix))

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            lower, upper = lu_factorization(matrix)
        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

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

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            lower, diag, upper = ldu_factorization(matrix)
        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

    def test_plu_factorization(self):
        matrix = Matrix([[1, 5, 4], [3, 6, 4], [8, 2, 3]], fraction=True)
        permuted, lower, upper = plu_factorization(matrix)
        self.assertEqual(repr(permuted),
            "Matrix([['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']])")
        self.assertEqual(repr(lower),
            "Matrix([['1', '0', '0'], ['3', '1', '0'], ['8', '38/9', '1']])")
        self.assertEqual(repr(upper),
            "Matrix([['1', '5', '4'], ['0', '-9', '-8'], ['0', '0', '43/9']])")
        self.assertEqual(repr(lower * upper), repr(permuted * matrix))

        matrix = Matrix([[0, 5, 4], [3, 0, 4], [8, 2, 3]], fraction=True)
        permuted, lower, upper = plu_factorization(matrix)
        self.assertEqual(repr(permuted),
            "Matrix([['0', '1', '0'], ['1', '0', '0'], ['0', '0', '1']])")
        self.assertEqual(repr(lower),
            "Matrix([['1', '0', '0'], ['0', '1', '0'], ['8/3', '2/5', '1']])")
        self.assertEqual(repr(upper),
            "Matrix([['3', '0', '4'], ['0', '5', '4'], ['0', '0', '-139/15']])")
        self.assertEqual(repr(lower * upper), repr(permuted * matrix))

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            permuted, lower, upper = plu_factorization(matrix)
        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

    def test_ldlt_factorization(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], fraction=True)
        lower, diag, lower_t = ldlt_factorization(matrix)
        self.assertEqual(repr(lower), "None")
        self.assertEqual(repr(diag), "None")
        self.assertEqual(repr(lower_t), "None")

        matrix = Matrix([[1, 2, 3], [2, 1, 4], [3, 4, 1]], fraction=True)
        lower, diag, lower_t = ldlt_factorization(matrix)
        self.assertEqual(repr(lower),
            "Matrix([['1', '0', '0'], ['2', '1', '0'], ['3', '2/3', '1']])")
        self.assertEqual(repr(diag),
            "Matrix([['1', '0', '0'], ['0', '-3', '0'], ['0', '0', '-20/3']])")
        self.assertEqual(repr(lower_t), 
            "Matrix([['1', '2', '3'], ['0', '1', '2/3'], ['0', '0', '1']])")
        self.assertEqual(repr(lower * diag * lower_t), repr(matrix))

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            lower, diag, lower_t = ldlt_factorization(matrix)
        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

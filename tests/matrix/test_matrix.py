import unittest

from fractions import Fraction as F
from matrox.matrix import *

class TestRowOperations(unittest.TestCase):

    def test_leading_term_index(self):
        index = leading_term_index([0, 0, 0, 0, 1])
        self.assertEqual(index, 4)

        index = leading_term_index([0, 0, 0])
        self.assertEqual(index, -1)

    def test_is_zero_vector(self):
        is_zero = is_zero_vector([0, 0, 0, 0])
        self.assertEqual(is_zero, True)

        is_zero = is_zero_vector([0, 0, 0, 1])
        self.assertEqual(is_zero, False)

    def test_row_op_mult(self):
        matrix = Matrix([[1, 2], [3, 4]])
        row_i = 0
        k = 2
        c_matrix = row_op_mult(matrix, row_i, k)
        self.assertEqual(repr(c_matrix), "Matrix([[2, 4], [3, 4]])")

    def test_row_op_add(self):
        matrix = Matrix([[1, 2], [3, 4]])
        from_i = 0
        to_i = 1
        k = 2
        c_matrix = row_op_add(matrix, from_i, to_i, k)
        self.assertEqual(repr(c_matrix), "Matrix([[1, 2], [5, 8]])")

    def test_row_op_swap(self):
        matrix = Matrix([[1, 2], [3, 4]])
        row_i = 0
        row_j = 1
        c_matrix = row_op_swap(matrix, row_i, row_j)
        self.assertEqual(repr(c_matrix), "Matrix([[3, 4], [1, 2]])")



class TestMatrixOperations(unittest.TestCase):

    def test_num_rows(self):
        matrix = Matrix([[1, 2], [3, 4]])
        rows = num_rows(matrix)
        self.assertEqual(repr(rows), "2")

    def test_num_cols(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        cols = num_cols(matrix)
        self.assertEqual(repr(cols), "3")

    def test_zero_matrix(self):
        matrix = zero_matrix(2, 4)
        self.assertEqual(repr(matrix), "Matrix([[0, 0, 0, 0], [0, 0, 0, 0]])")

        matrix = zero_matrix(0, 0)
        self.assertEqual(repr(matrix), "Matrix([])")

    def test_indentity_matrix(self):
        matrix = identity_matrix(3)
        self.assertEqual(repr(matrix), 
            "Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])")

        matrix = identity_matrix(0)
        self.assertEqual(repr(matrix), "Matrix([])")

    def test_scalar_mult_matrix(self):
        matrix = Matrix([[1, 2], [3, 4]])
        scalar_matrix = scalar_mult_matrix(matrix, 2)
        self.assertEqual(repr(scalar_matrix), "Matrix([[2, 4], [6, 8]])")

        matrix = Matrix([[1, 2], [3, 4]])
        scalar_matrix = scalar_mult_matrix(matrix, 0)
        self.assertEqual(repr(scalar_matrix), "Matrix([[0, 0], [0, 0]])")

    def test_add_matrices(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[5, 6], [7, 8]])
        matrix_c = add_matrices(matrix_a, matrix_b)
        self.assertEqual(repr(matrix_c), "Matrix([[6, 8], [10, 12]])")

    def test_subtract_matrices(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[5, 6], [7, 8]])
        matrix_c = subtract_matrices(matrix_a, matrix_b)
        self.assertEqual(repr(matrix_c), "Matrix([[-4, -4], [-4, -4]])")

        matrix_d = subtract_matrices(matrix_b, matrix_a)
        self.assertEqual(repr(matrix_d), "Matrix([[4, 4], [4, 4]])")

    def test_multiply_matrices(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[1, 2, 3], [4, 5, 6]])
        matrix_c = multiply_matrices(matrix_a, matrix_b)
        self.assertEqual(repr(matrix_c), "Matrix([[9, 12, 15], [19, 26, 33]])")

    def test_matrix_power(self):
        matrix = Matrix([[1, 2], [3, 4]])
        powered = matrix_power(matrix, 0)
        self.assertEqual(repr(powered), "Matrix([[1, 0], [0, 1]])")

        matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        powered = matrix ** 3
        self.assertEqual(repr(powered), 
            "Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])")



class TestMatrixFunctions(unittest.TestCase):

    def test_gaussian_elimination(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        c_matrix = gaussian_elimination(matrix)
        self.assertEqual(repr(c_matrix), 
            "Matrix([[1.0, 0.0, -1.0], [-0.0, 1.0, 2.0]])")

    def test_rref(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        c_matrix = rref(matrix)
        self.assertEqual(repr(c_matrix), 
            "Matrix([[1.0, 0.0, -1.0], [-0.0, 1.0, 2.0]])")

    def test_ref(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        c_matrix = ref(matrix)
        self.assertEqual(repr(c_matrix), 
            "Matrix([[1.0, 2.0, 3.0], [-0.0, 1.0, 2.0]])")

    def test_transpose(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        matrix_c = transpose(matrix)
        self.assertEqual(repr(matrix_c), "Matrix([[1, 4], [2, 5], [3, 6]])")

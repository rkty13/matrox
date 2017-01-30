import unittest

from matrox import *

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
        self.assertEqual(repr(matrix),
            "Matrix([['0', '0', '0', '0'], ['0', '0', '0', '0']])")

        matrix = zero_matrix(0, 0)
        self.assertEqual(repr(matrix), "Matrix([])")

    def test_indentity_matrix(self):
        matrix = identity_matrix(3)
        self.assertEqual(repr(matrix),
            "Matrix([['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']])")

        matrix = identity_matrix(0)
        self.assertEqual(repr(matrix), "Matrix([])")

    def test_scalar_mult_matrix(self):
        matrix = Matrix([[1, 2], [3, 4]])
        scalar_matrix = scalar_mult_matrix(matrix, 2)
        self.assertEqual(repr(scalar_matrix),
            "Matrix([['2', '4'], ['6', '8']])")

        matrix = Matrix([[1, 2], [3, 4]])
        scalar_matrix = scalar_mult_matrix(matrix, 0)
        self.assertEqual(repr(scalar_matrix),
            "Matrix([['0', '0'], ['0', '0']])")

    def test_add_matrices(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[5, 6], [7, 8]])
        matrix_c = add_matrices(matrix_a, matrix_b)
        self.assertEqual(repr(matrix_c), "Matrix([['6', '8'], ['10', '12']])")
        self.assertEqual(repr(matrix_a + matrix_b),
            "Matrix([['6', '8'], ['10', '12']])")

    def test_subtract_matrices(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[5, 6], [7, 8]])
        matrix_c = subtract_matrices(matrix_a, matrix_b)
        self.assertEqual(repr(matrix_c), "Matrix([['-4', '-4'], ['-4', '-4']])")
        self.assertEqual(repr(matrix_a - matrix_b),
            "Matrix([['-4', '-4'], ['-4', '-4']])")

        matrix_d = subtract_matrices(matrix_b, matrix_a)
        self.assertEqual(repr(matrix_d), "Matrix([['4', '4'], ['4', '4']])")
        self.assertEqual(repr(matrix_b - matrix_a),
            "Matrix([['4', '4'], ['4', '4']])")

    def test_multiply_matrices(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        matrix_b = Matrix([[1, 2, 3], [4, 5, 6]])
        matrix_c = multiply_matrices(matrix_a, matrix_b)
        self.assertEqual(repr(matrix_c),
            "Matrix([['9', '12', '15'], ['19', '26', '33']])")
        self.assertEqual(repr(matrix_a * matrix_b),
            "Matrix([['9', '12', '15'], ['19', '26', '33']])")

    def test_multiply_matrix_scalar(self):
        matrix_a = Matrix([[1, 2], [3, 4]])
        scalar = 2
        matrix_b = multiply_matrices(matrix_a, scalar)
        matrix_c = multiply_matrices(scalar, matrix_a)
        self.assertEqual(repr(matrix_b), "Matrix([['2', '4'], ['6', '8']])")
        self.assertEqual(repr(matrix_c), "Matrix([['2', '4'], ['6', '8']])")
        self.assertEqual(repr(matrix_a * scalar),
            "Matrix([['2', '4'], ['6', '8']])")
        self.assertEqual(repr(scalar * matrix_a),
            "Matrix([['2', '4'], ['6', '8']])")

    def test_matrix_power(self):
        matrix = Matrix([[1, 2], [3, 4]])
        powered = matrix_power(matrix, 0)
        self.assertEqual(repr(powered), "Matrix([['1', '0'], ['0', '1']])")

        matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        powered = matrix ** 3
        self.assertEqual(repr(powered),
            "Matrix([['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']])")



class TestMatrixFunctions(unittest.TestCase):

    def test_transpose(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        matrix_c = transpose(matrix)
        self.assertEqual(repr(matrix_c),
            "Matrix([['1', '4'], ['2', '5'], ['3', '6']])")

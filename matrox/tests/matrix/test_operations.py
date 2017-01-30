import unittest

from matrox import *

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
        matrix = Matrix([[1, 2], [3, 4]], fraction=True)
        row_i = 0
        k = 2
        c_matrix = row_op_mult(matrix, row_i, k)
        self.assertEqual(repr(c_matrix), "Matrix([['2', '4'], ['3', '4']])")

    def test_row_op_add(self):
        matrix = Matrix([[1, 2], [3, 4]], fraction=True)
        from_i = 0
        to_i = 1
        k = 2
        c_matrix = row_op_add(matrix, from_i, to_i, k)
        self.assertEqual(repr(c_matrix), "Matrix([['1', '2'], ['5', '8']])")

    def test_row_op_swap(self):
        matrix = Matrix([[1, 2], [3, 4]], fraction=True)
        row_i = 0
        row_j = 1
        c_matrix = row_op_swap(matrix, row_i, row_j)
        self.assertEqual(repr(c_matrix), "Matrix([['3', '4'], ['1', '2']])")



class TestElementaryMatrixOperations(unittest.TestCase):

    def test_el_matrix_add(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        el_matrix = el_matrix_add(matrix, 1, 2, 2)
        self.assertEqual(repr(el_matrix), 
            "Matrix([['1', '0', '0'], ['0', '1', '2'], ['0', '0', '1']])")
        self.assertEqual(repr(el_matrix * matrix),
            "Matrix([['1', '2', '3'], ['18', '21', '24'], ['7', '8', '9']])")

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            el_matrix = el_matrix_add(matrix, 1, 1, 2)
        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

    def test_el_matrix_mult(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        el_matrix = el_matrix_mult(matrix, 1, 2)
        self.assertEqual(repr(el_matrix), 
            "Matrix([['1', '0', '0'], ['0', '2', '0'], ['0', '0', '1']])")
        self.assertEqual(repr(el_matrix * matrix),
            "Matrix([['1', '2', '3'], ['8', '10', '12'], ['7', '8', '9']])")

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            el_matrix = el_matrix_mult(matrix, 1, 1)
        self.assertTrue("Matrix must be a square matrix." in str(c.exception))

    def test_el_matrix_swap(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        el_matrix = el_matrix_swap(matrix, 1, 2)
        self.assertEqual(repr(el_matrix), 
            "Matrix([['1', '0', '0'], ['0', '0', '1'], ['0', '1', '0']])")
        self.assertEqual(repr(el_matrix * matrix),
            "Matrix([['1', '2', '3'], ['7', '8', '9'], ['4', '5', '6']])")

        matrix = Matrix([[1, 1, 1], [1, 1, 1]])
        with self.assertRaises(DimensionError) as c:
            el_matrix = el_matrix_swap(matrix, 0, 1)
        self.assertTrue("Matrix must be a square matrix." in str(c.exception))
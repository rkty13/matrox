import unittest
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

import unittest

from matrox import Matrix
from matrox.linalg import *

class TestElementaryMatrixOperations(unittest.TestCase):

    def test_el_matrix_add(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        el_matrix = el_matrix_add(matrix, 1, 2, 2)
        self.assertEqual(repr(el_matrix), 
            "Matrix([['1', '0', '0'], ['0', '1', '2'], ['0', '0', '1']])")
        self.assertEqual(repr(el_matrix * matrix),
            "Matrix([['1', '2', '3'], ['18', '21', '24'], ['7', '8', '9']])")

    def test_el_matrix_mult(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        el_matrix = el_matrix_mult(matrix, 1, 2)
        self.assertEqual(repr(el_matrix), 
            "Matrix([['1', '0', '0'], ['0', '2', '0'], ['0', '0', '1']])")
        self.assertEqual(repr(el_matrix * matrix),
            "Matrix([['1', '2', '3'], ['8', '10', '12'], ['7', '8', '9']])")

    def test_el_matrix_swap(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        el_matrix = el_matrix_swap(matrix, 1, 2)
        self.assertEqual(repr(el_matrix), 
            "Matrix([['1', '0', '0'], ['0', '0', '1'], ['0', '1', '0']])")
        self.assertEqual(repr(el_matrix * matrix),
            "Matrix([['1', '2', '3'], ['7', '8', '9'], ['4', '5', '6']])")
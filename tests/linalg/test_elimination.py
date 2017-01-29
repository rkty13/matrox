import unittest

from matrox import Matrix
from matrox.linalg import *

class TestMatrixElimination(unittest.TestCase):

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

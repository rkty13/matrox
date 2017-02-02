import unittest

from matrox import Matrix, fill_matrix
from matrox.linalg import *

class TestProperties(unittest.TestCase):

    def test_rank(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        matrix_rank = rank(matrix)
        self.assertEqual(repr(matrix_rank), "2")

        matrix = fill_matrix(3, 3, 2)
        matrix_rank = rank(matrix)
        self.assertEqual(repr(matrix_rank), "1")
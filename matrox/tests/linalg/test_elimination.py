import unittest

from matrox import Matrix
from matrox.linalg import *

class TestMatrixElimination(unittest.TestCase):

    def test_gaussian_elimination(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]], fraction=True)
        c_matrix, traceback, inverse_traceback = gaussian_elimination(matrix)
        self.assertEqual(repr(c_matrix), 
            "Matrix([['1', '0', '-1'], ['0', '1', '2']])")
        self.assertEqual(repr(traceback), "[]")
        self.assertEqual(repr(inverse_traceback), "[]")

        matrix = Matrix([[4, 7], [2, 6]], fraction=True)
        c_matrix, traceback, inverse_traceback = gaussian_elimination(matrix, 
            history=True)
        self.assertEqual(repr(c_matrix),
            "Matrix([['1', '0'], ['0', '1']])")
        self.assertEqual(repr(traceback),
            "[Matrix([['1/4', '0'], ['0', '1']]), " +
            "Matrix([['1', '0'], ['-2', '1']]), " +
            "Matrix([['1', '0'], ['0', '2/5']]), " +
            "Matrix([['1', '-7/4'], ['0', '1']])]")
        self.assertEqual(repr(inverse_traceback), "[]")

        matrix = Matrix([[4, 7], [2, 6]], fraction=True)
        c_matrix, traceback, inverse_traceback = gaussian_elimination(matrix, 
            inverse_history=True)
        self.assertEqual(repr(c_matrix),
            "Matrix([['1', '0'], ['0', '1']])")
        self.assertEqual(repr(traceback), "[]")
        self.assertEqual(repr(inverse_traceback),
            "[Matrix([['4', '0'], ['0', '1']]), " +
            "Matrix([['1', '0'], ['2', '1']]), " +
            "Matrix([['1', '0'], ['0', '5/2']]), " +
            "Matrix([['1', '7/4'], ['0', '1']])]")

        matrix = Matrix([[0, 0, 0], [3, 2, 1]], fraction=True)
        c_matrix, traceback, inverse_traceback = gaussian_elimination(matrix,
            history=True, inverse_history=True)
        self.assertEqual(repr(c_matrix),
            "Matrix([['1', '2/3', '1/3'], ['0', '0', '0']])")


    def test_rref(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]], fraction=True)
        c_matrix, traceback, inverse_traceback = rref(matrix)
        self.assertEqual(repr(c_matrix), 
            "Matrix([['1', '0', '-1'], ['0', '1', '2']])")
        self.assertEqual(repr(traceback), "[]")
        self.assertEqual(repr(inverse_traceback), "[]")

    def test_ref(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6]], fraction=True)
        c_matrix, traceback, inverse_traceback = ref(matrix)
        self.assertEqual(repr(c_matrix), 
            "Matrix([['1', '2', '3'], ['0', '1', '2']])")
        self.assertEqual(repr(traceback), "[]")
        self.assertEqual(repr(inverse_traceback), "[]")

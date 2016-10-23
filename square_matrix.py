from matrix import Matrix
from exceptions import DimensionError
from copy import deepcopy

class SquareMatrix(Matrix):
    def __init__(self, size = 0, rows = 0, cols = 0, lst = None, fractional = True, identity = False):
        if size and (rows or cols):
            raise ValueError("Specified size is ambiguous. Please use either size or rows/cols.")
        if rows != cols:
            raise DimensionError("Square matrices must have n rows and columns.")
        if lst and len(lst) != len(lst[0]):
            raise DimensionError("Square matrices must have n x n dimensions.")
        if identity:
            dim = size if size else rows
            lst = [[1 if i == r else 0 for i in range(dim)] for r in range(dim)]
        super().__init__(rows = size if size else rows, cols = size if size else cols, 
                            lst = lst, fractional = fractional)

    def determinant(self):
        B = self.lu_decomposition()
        l, u = 1, 1
        for i in range(len(self._m)):
            l *= B[0][i][i]
            u *= B[1][i][i]
        return l * u

    def inverse(self):
        pass

    def upper_triangular(self, history = False, inverse_history = False):
        B = deepcopy(self)
        traceback = []
        inverse_traceback = []
        i = 0
        while i < len(B):
            j = i + 1
            while j < len(B):
                if j == i:
                    j += 1
                    continue
                s = 1 if B[i][i] < 0 == B[j][i] < 0 else -1
                multiple = s * B[j][i] / B[i][i]
                B = self._row_op_add(B, i, j, multiple)
                if history:
                    t = SquareMatrix(size = len(self._m), identity = True)
                    t[j][i] = deepcopy(multiple)
                    traceback.append(t)
                if inverse_history:
                    t = SquareMatrix(size = len(self._m), identity = True)
                    t[j][i] = deepcopy(-multiple)
                    inverse_traceback.append(t)
                j += 1
            i += 1
        return B, traceback, inverse_traceback

    def lower_triangular(self, history = False, inverse_history = False):
        B = deepcopy(self)
        traceback = []
        inverse_traceback = []
        i = len(B) - 1
        while i >= 0:
            j = i - 1
            while j >= 0:
                if j == i:
                    j -= 1
                    continue
                s = 1 if B[i][i] < 0 == B[j][i] < 0 else -1
                multiple = s * B[j][i] / B[i][i]
                B = self._row_op_add(B, i, j, multiple)
                if history:
                    t = SquareMatrix(size = len(self._m), identity = True)
                    t[j][i] = deepcopy(multiple)
                    traceback.append(t)
                if inverse_history:
                    t = SquareMatrix(size = len(self._m), identity = True)
                    t[j][i] = deepcopy(-multiple)
                    inverse_traceback.append(t)
                j -= 1
            i -= 1
        return B, traceback, inverse_traceback

    def lu_decomposition(self):
        B = self.upper_triangular(inverse_history = True)
        C = SquareMatrix(size = len(self._m), identity = True)
        for i in range(len(B[2])):
            C *= B[2][i]
        return C, B[0]

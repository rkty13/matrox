from linear_system import LinearSystem
from vector import Vector
from exceptions import DimensionError
from square_matrix import SquareMatrix
from copy import deepcopy

class SquareLinearSystem(LinearSystem):
    def __init__(self, unknowns = 0, A = None, b = None, fractional = True):
        if A and not isinstance(A, SquareMatrix):
            raise TypeError("A must be of type SquareMatrix.")
        if b and not isinstance(b, Vector):
            raise TypeError("b must be of type Vector.")

        if A and b and len(A._m) != len(b):
            raise DimensionError("The number of equations must be " + 
                                    "the same as the number of unknowns.")
        super().__init__(equations = unknowns, unknowns = unknowns, 
                            A = A, b = b, fractional = fractional)

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
        tb = []
        i_tb = []
        i = len(B) - 1
        while i >= 0:
            j = i - 1
            while j >= 0:
                if j == i:
                    j -= 1
                    continue
                s = 1 if B[i][i] < 0 == B[j][i] < 0 else -1
                m = s * B[j][i] / B[i][i]
                B = self._row_op_add(B, i, j, m)
                if history:
                    t = SquareMatrix(size = len(self._m), identity = True)
                    t[j][i] = deepcopy(m)
                    tb.append(t)
                if inverse_history:
                    t = SquareMatrix(size = len(self._m), identity = True)
                    t[j][i] = deepcopy(-m)
                    i_tb.append(t)
                j -= 1
            i -= 1
        return B, tb, i_tb

    def _row_op_mult(self, LS, row_i, k):
        new_LS = deepcopy(LS)
        new_LS._A = new_LS._A._row_op_mult(new_LS._A, row_i, k)
        new_LS._b = new_LS._b._row_op_mult(new_LS._b, row_i, k)
        return new_LS

    def _row_op_swap(self, LS, row_i, row_j):
        new_LS = deepcopy(LS)
        new_LS._A = new_LS._A._row_op_swap(new_LS._A, row_i, row_j)
        new_LS._b = new_LS._b._row_op_swap(new_LS._b, row_i, row_j)
        return new_LS

    def _row_op_add(self, LS, from_i, to_i, k):
        new_LS = deepcopy(LS)
        new_LS._A = new_LS._A._row_op_add(new_LS._A, from_i, to_i, k)
        new_LS._b = new_LS._b._row_op_add(new_LS._b, from_i, to_i, k)
        return new_LS

    def __copy__(self):
        LS = type(self)()
        LS._A = self._A
        LS._b = self._b
        return LS

    def __deepcopy__(self, memo):
        LS = type(self)()
        LS._A = deepcopy(self._A, memo)
        LS._b = deepcopy(self._b, memo)
        return LS

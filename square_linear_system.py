from linear_system import LinearSystem
from exceptions import DimensionError
from square_matrix import SquareMatrix

class SquareLinearSystem(LinearSystem):
    def __init__(unknowns = 0, A = None, b = None, fractional = True):
        if A and not isinstance(A, SquareMatrix):
            raise TypeError("A must be of type SquareMatrix.")
        if b and not isinstance(b, Vector):
            raise TypeError("b must be of type Vector.")

        if A and b and len(A[m]) != len(b):
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

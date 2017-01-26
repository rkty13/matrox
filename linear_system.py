from matrix import Matrix
from square_matrix import SquareMatrix
from vector import Vector
from exceptions import DimensionError
from copy import deepcopy

class LinearSystem(Matrix):
    def __init__(self, rows = 0, cols = 0, A = None, b = None, fractional = True):
        super().__init__(rows = rows, cols = cols, lst = A, fractional = fractional)
        self._b = deepcopy(b) if b else \
                    Vector(length = rows, fractional = fractional)

    def rref(self):
        return self._gauss_jordan_elimination(reduced = True)

    def simplify(self):
        new_LS = deepcopy(self)
        i = 0
        while i < len(new_LS):
            f = self[i].leading_term_index()
            if f < 0:
                i += 1
                continue
            new_LS = self._row_op_mult(new_LS, i, 1 / new_LS[i][f])
            i += 1
        return new_LS

    def _row_op_mult(self, LS, row_i, k):
        new_LS = deepcopy(LS)
        self = self._row_op_mult(self, row_i, k)
        new_LS._b = new_LS._b._row_op_mult(new_LS._b, row_i, k)
        return new_LS

    def _row_op_swap(self, LS, row_i, row_j):
        new_LS = deepcopy(LS)
        self = self._row_op_swap(self, row_i, row_j)
        new_LS._b = new_LS._b._row_op_swap(new_LS._b, row_i, row_j)
        return new_LS

    def _row_op_add(self, LS, from_i, to_i, k):
        new_LS = deepcopy(LS)
        self = self._row_op_add(self, from_i, to_i, k)
        new_LS._b = new_LS._b._row_op_add(new_LS._b, from_i, to_i, k)
        return new_LS

    def _gauss_jordan_elimination(self, reduced = True):
        B = deepcopy(self)
        i = 0
        while i < len(B):
            f = B[i].leading_term_index()
            if f < 0:
                i += 1
                continue
            B = self._row_op_mult(B, i, 1 / B[i][f])
            j = 0 if reduced else i + 1
            while j < len(B):
                if j == i:
                    j += 1
                    continue
                s = 1 if B[i][f] < 0 == B[j][f] < 0 else -1
                B = self._row_op_add(B, i, j, s * B[j][f] / B[i][f])
                if B[j].is_zero_vector():
                    for h in range(j + 1, len(B)):
                        B = self._row_op_swap(B, h - 1, h)
                j += 1
            i += 1
        return B.simplify()

    def __len__(self):
        return len(self._m)

    def __str__(self):
        return str({"A": str(self._m), "b": str(self._b)})

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, x):
        return Vector(lst = list(self._m[x]) + [self._b[x]])

    def __copy__(self):
        LS = type(self)()
        LS._m = self._m
        LS._b = self._b
        return LS

    def __deepcopy__(self, memo):
        return type(self)(rows = self._rows, cols = self._cols, A = self._m, b = self._b, fractional = self._fractional)      
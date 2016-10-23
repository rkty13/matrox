from vector import Vector
from element import Element
from fraction import Fraction as F
from exceptions import DimensionError
from copy import deepcopy

class Matrix(object):
    def __init__(self, rows = 0, cols = 0, lst = None, fractional = True):
        self._fractional = fractional
        if lst is not None:
            if type(lst) is not list:
                raise TypeError("lst is not of type list.")
        self._m = []
        for m in range(len(lst) if lst else rows):
            if lst:
                self._m.append(Vector(lst = lst[m], fractional = self._fractional))
            else:
                self._m.append(Vector(length = cols, fractional = self._fractional))
        self._rows = len(lst) if lst else rows
        self._cols = len(lst[m]) if lst else cols

    def num_rows(self):
        return self._rows

    def num_cols(self):
        return self._cols

    def rref(self):
        return self._gauss_jordan_elimination(reduced = True)

    def ref(self):
        return self._gauss_jordan_elimination(reduced = False)

    def simplify(self):
        B = deepcopy(self)
        i = 0
        while i < len(B):
            f = B[i].leading_term_index()
            if f < 0:
                i += 1
                continue
            B = self._row_op_mult(B, i, 1 / B[i][f])
            i += 1
        return B

    def _scalar_mult(self, k, A):
        B = deepcopy(self)
        for m in range(len(A)):
            for n in range(len(A[m])):
                B[m][n] = A[m][n] * k
        return B

    def _addition(self, A, B):
        if A.num_rows() != B.num_rows() or A.num_cols() != B.num_cols():
            raise DimensionError("Dimensions do not match")
        C = deepcopy(self)
        for m in range(A.num_rows()):
            for n in range(A.num_cols()):
                C[m][n] = A[m][n] + B[m][n]
        return C

    def _subtraction(self, A, B):
        t = self._scalar_mult(-1, B)
        return self._addition(A, t)

    def transpose(self):
        B = deepcopy(self)
        for m in range(len(self)):
            for n in range(len(self[m])):
                B[n][m] = self[m][n]
        return B

    def _multiplication(self, A, B):
        if A.num_cols() != B.num_rows():
            raise DimensionError("The dimensions of the two matrices do not match.")
        if type(B) in (int, float):
            return self._scalar_mult(B, A)
        C = deepcopy(self)
        for i in range(A.num_rows()):
            for j in range(B.num_cols()):
                el_sum = 0
                for k in range(A.num_cols()):
                    el_sum += A[i][k] * B[k][j]
                C[i][j] = el_sum
        return C

    def _power(self, A, k):
        if k < 0:
            raise ValueError("Power cannot be less than 0.")
        if k == 0:
            C = deepcopy(self)
            for i in range(C.num_rows()):
                C[i][i] = 1
            return C
        C = deepcopy(A)
        for i in range(k - 1):
            C = C * A
        return C

    def _row_op_mult(self, A, row_i, k):
        B = deepcopy(A)
        B[row_i] *= k
        return B

    def _row_op_swap(self, A, row_i, row_j):
        B = deepcopy(A)
        B[row_i], B[row_j] = B[row_j], B[row_i]
        return B

    def _row_op_add(self, A, from_i, to_i, k):
        B = deepcopy(A)
        B[to_i] += B[from_i] * k
        return B

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

    def __getitem__(self, x):
        return self._m[x]

    def __setitem__(self, key, value):
        self._m[key] = value

    def __len__(self):
        return len(self._m)

    def __str__(self):
        return str(self._m)

    def __repr__(self):
        return self.__str__()

    def __add__(self, B):
        return self._addition(self, B)

    def __radd__(self, B):
        return self._addition(self, B)

    def __iadd__(self, B):
        return self + B

    def __sub__(self, B):
        return self._subtraction(self, B)

    def __rsub__(self, B):
        return self._subtraction(B, self)

    def __isub__(self, B):
        return self - B

    def __mul__(self, B):
        return self._multiplication(self, B)

    def __rmul__(self, B):
        return self._multiplication(B, self)

    def __imul__(self, B):
        return self * B

    def __pow__(self, x):
        return self._power(self, x)

    def __copy__(self):
        m = type(self)(rows = self._rows, cols = self._cols, fractional = self._fractional)
        m._m = self._m
        return m

    def __deepcopy__(self, memo):
        m = type(self)(fractional = self._fractional)
        for i in range(len(self._m)):
            m._m.append(deepcopy(self._m[i], memo))
        m._rows = self._rows
        m._cols = self._cols
        return m
from vector import Vector
from exceptions import DimensionError

class Matrix(object):
    def __init__(self, rows = 0, cols = 0, copy = None):
        if copy is not None:
            if type(copy) is not list and type(copy) is not Matrix:
                raise TypeError("copy is not of type list or Matrix.")
        self._m = []
        for m in range(len(copy) if copy else rows):
            self._m.append(Vector())
            for n in range(len(copy[m]) if copy else cols):
                self._m[m].append(copy[m][n] if copy else 0)
        self._rows = len(copy) if copy else rows
        self._cols = len(copy[m]) if copy else cols

    def num_rows(self):
        return self._rows

    def num_cols(self):
        return self._cols

    def rref(self):
        return self._gauss_jordan_elimination()

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

    def _scalar_mult(self, k, A):
        B = Matrix(rows = A.num_rows(), cols = A.num_cols())
        for m in range(len(A)):
            for n in range(len(A[m])):
                B[m][n] = A[m][n] * k
        return B

    def _addition(self, A, B):
        if A.num_rows() != B.num_rows() or A.num_cols() != B.num_cols():
            raise DimensionError("Dimensions do not match")
        C = Matrix(rows = len(A), cols = len(A[0]))
        for m in range(A.num_rows()):
            for n in range(A.num_cols()):
                C[m][n] = A[m][n] + B[m][n]
        return C

    def _subtraction(self, A, B):
        t = self._scalar_mult(-1, B)
        return self._addition(A, t)

    def transpose(self):
        B = Matrix(rows = self.num_cols(), cols = self.num_rows())
        for m in range(len(self)):
            for n in range(len(self[m])):
                B[n][m] = self[m][n]
        return B

    def _multiplication(self, A, B):
        if A.num_cols() != B.num_rows():
            raise DimensionError("The dimensions of the two matrices do not match.")
        if type(B) is int:
            return self._scalar_mult(B, A)
        C = Matrix(rows = A.num_rows(), cols = B.num_cols())
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
            C = Matrix(rows = A.num_rows(), cols = A.num_cols())
            for i in range(C.num_rows()):
                C[i][i] = 1
            return C
        C = Matrix(copy = A)
        for i in range(k - 1):
            C = C * A
        return C

    def _row_op_scalar_mult(self, A, row_i, k):
        v = Vector(copy = A[row_i])
        return v * k

    def _row_op_swap(self, A, row_i, row_j):
        B = Matrix(copy = A)
        B[row_i], B[row_j] = B[row_j], B[row_i]
        return B

    def _row_op_factor_add(self, A, from_i, to_i, k):
        v = Vector(copy = A[to_i])
        v += A[from_i] * k
        return v

    def _gauss_jordan_elimination(self):
        B = Matrix(copy = self)
        i = 0
        while i < len(B):
            f = B[i].leading_term_index()
            if f < 0:
                i += 1
                continue
            k_factor = 1 / B[i][f]
            B[i] = self._row_op_scalar_mult(B, i, k_factor)
            j = 0
            while j < len(B):
                if j == i:
                    j += 1
                    continue
                sign = 1 if B[i][f] < 0 == B[j][f] < 0 else -1
                q_factor = sign * B[j][f] / B[i][f]
                B[j] = self._row_op_factor_add(B, i, j, q_factor)
                if B[j].is_zero_vector():
                    for h in range(j + 1, len(B)):
                        B = self._row_op_swap(B, h - 1, h)
                j += 1
            i += 1
        return B

class SquareMatrix(Matrix):
    def __init__(self, rows = 0, cols = 0, copy = None):
        super().__init__(rows = rows, cols = cols, copy = copy)

    def determinant(self):
        pass

    def inverse(self):
        pass

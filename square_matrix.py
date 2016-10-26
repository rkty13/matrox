from matrix import Matrix
from exceptions import DimensionError
from exceptions import DoesNotExistError
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
        L, U = self.lu_factorization()
        l, u = 1, 1
        for i in range(len(self._m)):
            l *= L[i][i]
            u *= U[i][i]
        return l * u

    def rref(self):
        return self._gauss_jordan_elimination(reduced = True)

    def ref(self):
        return self._gauss_jordan_elimination(reduced = False)

    def inverse(self):
        B = self._gauss_jordan_elimination(reduced = True, history = True)
        if B[0].is_identity():
            C = SquareMatrix(size = len(self._m), identity = True)
            for i in range(len(B[1]) - 1, -1, -1):
                C *= B[1][i]
            return C
        else:
            return None

    def is_identity(self):
        for i in range(len(self._m)):
            for j in range(len(self._m[i])):
                if i == j and self._m[i][j] != 1:
                    return False
                if i != j and self._m[i][j] != 0:
                    return False
        return True

    def is_symmetric(self):
        for i in range(len(self._m)):
            for j in range(i, len(self._m[i])):
                if self._m[i][j] != self._m[j][i]:
                    return False
        return True

    def permute(self, A):
        P = SquareMatrix(size = len(A._m), identity = True)
        PA = deepcopy(A)
        for i in range(len(PA)):
            if PA[i][i] == 0:
                s = i + 1
                while s < len(PA):
                    if PA[s][i] != 0:
                        break
                    else:
                        s += 1
                if s < len(PA):
                    P = P._el_matrix_swap(i, s)
                    PA = PA._el_matrix_swap(i, s)
        return P

    def lu_factorization(self):
        B = self.upper_triangular(inverse_history = True)
        U = B[0]
        L = SquareMatrix(size = len(self._m), identity = True)
        for i in range(len(B[2])):
            L *= B[2][i]
        return L, U

    def ldu_factorization(self):
        L, U = self.lu_factorization()
        D = SquareMatrix(size = len(self._m), identity = True)
        for i in range(len(D)):
            D[i][i] = deepcopy(U[i][i])
            U = U._row_op_mult(U, i, 1 / U[i][i])
        return L, D, U

    def plu_factorization(self):
        P = self.permute(self)
        L, U = (P * self).lu_factorization()
        return P, L, U

    def ldlt_factorization(self):
        if not self.is_symmetric():
            return None, None, None
        return self.ldu_factorization()

    def upper_triangular(self, history = False, inverse_history = False):
        B = deepcopy(self)
        tb = []
        i_tb = []
        i = 0
        while i < len(B):
            j = i + 1
            while j < len(B):
                if j == i:
                    j += 1
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
                j += 1
            i += 1
        return B, tb, i_tb

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

    def _el_matrix_add(self, i, j, k):
        t = SquareMatrix(size = len(self._m), identity = True)
        t[i][j] = deepcopy(k)
        return t

    def _el_matrix_mult(self, i, k):
        t = SquareMatrix(size = len(self._m), identity = True)
        t[i][i] = deepcopy(k)
        return t

    def _el_matrix_swap(self, i, j):
        t = SquareMatrix(size = len(self._m), identity = True)
        t[i], t[j] = t[j], t[i]
        return t

    def _gauss_jordan_elimination(self, reduced = True, history = False, inverse_history = False):
        B = deepcopy(self)
        tb = []
        i_tb = []
        i = 0
        while i < len(B):
            f = B[i].leading_term_index()
            if f < 0:
                i += 1
                continue
            r = 1 / B[i][f]
            B = self._row_op_mult(B, i, r)
            if history:
                tb.append(self._el_matrix_mult(i, r))
            if inverse_history:
                i_tb.append(self._el_matrix_mult(i, 1 / r))
            j = 0 if reduced else i + 1
            while j < len(B):
                if j == i:
                    j += 1
                    continue
                s = 1 if B[i][f] < 0 == B[j][f] < 0 else -1
                m = s * B[j][f] / B[i][f]
                B = self._row_op_add(B, i, j, m)
                if history:
                    tb.append(self._el_matrix_add(j, i, m))
                if inverse_history:
                    i_tb.append(self._el_matrix_add(j, i, -m))
                if B[j].is_zero_vector():
                    for h in range(j + 1, len(B)):
                        B = self._row_op_swap(B, h - 1, h)
                        if history:
                            tb.append(self._el_matrix_swap(h - 1, h))
                        if inverse_history:
                            i_tb.append(self._el_matrix_swap(h - 1, h))
                j += 1
            i += 1
        return B.simplify(), tb, i_tb

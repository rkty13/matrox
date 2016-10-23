from element import Element
from fraction import Fraction as F
from exceptions import DimensionError
from copy import deepcopy

class Vector(object):
    def __init__(self, length = 0, lst = None, fractional = False):
        self._fractional = fractional
        if lst:
            self._v = [F(deepcopy(x)) if self._fractional else deepcopy(x) for x in lst]
        else:
            self._v = [F(0) if self._fractional else 0 for _ in range(length)]

    def append(self, x):
        self._v.append(x)

    def leading_term_index(self):
        for i in range(len(self._v)):
            if self._v[i] != 0:
                return i
        return -1

    def is_zero_vector(self):
        return self.leading_term_index() < 0

    def _scalar_mult(self, k, A):
        Q = deepcopy(A)
        for m in range(len(Q)):
            Q[m] *= k
        return Q

    def _addition(self, A, B):
        if len(A) != len(B):
            raise DimensionError("Dimensions do not match")
        C = deepcopy(A)
        for m in range(len(A)):
            C[m] = A[m] + B[m]
        return C

    def _subtraction(self, A, B):
        t = self._scalar_mult(-1, B)
        return self._addition(A, t)

    def _multiplication(self, A, B):
        if type(B) in (int, float) or isinstance(B, Element):
            return self._scalar_mult(B, A)
        if len(A) != len(B):
            raise DimensionError("The dimensions of the two matrices do not match.")
        val = 0
        for m in range(len(A)):
            val += A[m] * B[m]
        return val

    def _row_op_mult(self, b, row_i, k):
        v = deepcopy(b)
        v[row_i] *= k
        return v

    def _row_op_swap(self, b, row_i, row_j):
        v = deepcopy(b)
        v[row_i], v[row_j] = v[row_j], v[row_i]
        return v

    def _row_op_add(self, b, from_i, to_i, k):
        v = deepcopy(b)
        v[to_i] += v[from_i] * k
        return v

    def __iter__(self):
        for i in self._v:
            yield i

    def __getitem__(self, x):
        return self._v[x]

    def __setitem__(self, key, value):
        self._v[key] = value

    def __len__(self):
        return len(self._v)

    def __str__(self):
        return str(self._v)

    def __repr__(self):
        return self.__str__()

    def __add__(self, B):
        return self._addition(self, B)

    def __radd__(self, B):
        return self._addition(B, self)

    def __iadd__(self, B):
        return self._addition(self, B)

    def __sub__(self, B):
        return self._subtraction(self, B)

    def __rsub__(self, B):
        return self._subtraction(B, self)

    def __isub__(self, B):
        return self._subtraction(self, B)

    def __mul__(self, B):
        return self._multiplication(self, B)

    def __rmul__(self, B):
        return self._multiplication(B, self)

    def __imul__(self, B):
        return self._multiplication(self, B)

    def __copy__(self):
        v = type(self)(fractional = self._fractional)
        v._v = self._v
        return v

    def __deepcopy__(self, memo):
        v = type(self)(fractional = self._fractional)
        v._v = [deepcopy(self._v[x], memo) for x in range(len(self._v))]
        return v
        
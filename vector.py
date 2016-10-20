from element import Element
from fraction import Fraction as F

class Vector(object):
    def __init__(self, length = 0, copy = None, fractional = False):
        if copy is not None:
            if type(copy) is not list and type(copy) is not Vector:
                raise TypeError("copy is not of type list or Vector.")
        self._v = []
        for m in range(len(copy) if copy else length):
            if fractional:
                self._v.append(F(copy[m]) if copy else F(0))
            self._v.append(copy[m] if copy else 0)

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
        Q = Vector(copy = A)
        for m in range(len(Q)):
            Q[m] *= k
        return Q

    def _addition(self, A, B):
        if len(A) != len(B):
            raise DimensionError("Dimensions do not match")
        C = Vector(length = len(A))
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
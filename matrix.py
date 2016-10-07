from vector import Vector

class Matrix(object):
    def __init__(self, rows = 0, cols = 0, copy = None):
        if copy is not None:
            if type(copy) is not list and type(copy) is not Matrix:
                raise TypeError("copy is not of type list or Matrix.")

        self._m = []
        for m in range(len(copy) if copy else rows):
            self._m.append(Vector())
            for n in range(len(copy) if copy else cols):
                self._m[m].append(copy[m][n] if copy else 0)
        self._rows = len(copy) if copy else rows
        self._cols = len(copy) if copy else cols

    def num_rows(self):
        return self._rows

    def num_cols(self):
        return self._cols

    def __getitem__(self, x):
        return self._m[x]

    def __len__(self):
        return len(self._m)

    def __str__(self):
        return str(self._m)

    def __repr__(self):
        return self.__str__()

    def __add__(self, B):
        return self.addition(self, B)

    def __radd__(self, B):
        return self.addition(self, B)

    def __iadd__(self, B):
        pass

    def __sub__(self, B):
        return self.subtraction(self, B)

    def __rsub__(self, B):
        return self.subtraction(B, self)

    def __isub__(self, B):
        pass

    def __mul__(self, B):
        pass

    def __rmul__(self, B):
        pass

    def __imul__(self, B):
        pass

    def scalar_mult(self, k, A):
        B = Matrix(rows = A.num_rows(), cols = A.num_cols())
        for m in range(len(A)):
            for n in range(len(A[m])):
                B[m][n] = A[m][n] * k
        return B

    def addition(self, A, B):
        if len(A) != len(B) and len(A[0]) != len(B[0]):
            raise DimensionError("Dimensions do not match")
        C = Matrix(rows = len(A), cols = len(A[0]))
        for m in range(A.num_rows()):
            for n in range(A.num_cols()):
                C[m][n] = A[m][n] + B[m][n]
        return C

    def subtraction(self, A, B):
        t = self.scalar_mult(-1, B)
        return self.addition(A, t)

    def transpose(self):
        B = Matrix(rows = self.num_cols(), cols = self.num_rows())
        for m in range(len(self)):
            for n in range(len(self[m])):
                B[n][m] = self[m][n]
        return B







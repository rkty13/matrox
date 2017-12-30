from copy import deepcopy
from matrox import Matrix

class Vector(Matrix):
    def __init__(self, data, fraction=False):
        self._matrix = []
        for i in range(len(data)):
            if fraction:
                self._matrix.append([Fraction(data[i])])
            else:
                self._matrix.append([deepcopy(data[i])])

    def __getitem__(self, key):
        return self._matrix[key][0]

    def __setitem__(self, key, value):
        self._matrix[key][0] = value

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__,
            str([str(i[0]) for i in self._matrix]))

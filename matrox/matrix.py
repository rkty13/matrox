from copy import deepcopy
from .elements.element import Element

class Matrix(object):
    def __init__(self, data):
        self._matrix = []
        for i in range(len(data)):
            self._matrix.append([])
            for j in range(len(data[i])):
                self._matrix[i].append(deepcopy(data[i][j]))

    def __getitem__(self, key):
        return self._matrix[key]

    def __setitem__(self, key, value):
        self._matrix[key] = value

    def __len__(self):
        return len(self._matrix)

    def __deepcopy__(self, memo):
        return type(self)(self._matrix)

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__, str(self._matrix))



def leading_term_index(vector):
    for i in range(len(vector)):
        if vector[i] != 0:
            return i
    return -1

def is_zero_vector(vector):
    return leading_term_index(vector) < 0

def row_op_mult(matrix, row_i, k):
    cmatrix = deepcopy(matrix)
    cmatrix[row_i] = list(map(lambda x: x * k, cmatrix[row_i]))
    return cmatrix

def row_op_add(matrix, from_i, to_i, k):
    cmatrix = deepcopy(matrix)
    cmatrix[to_i] = [x * k + y for x, y in zip(cmatrix[from_i], cmatrix[to_i])]
    return cmatrix

def row_op_swap(matrix, row_i, row_j):
    cmatrix = deepcopy(matrix)
    cmatrix[row_i], cmatrix[row_j] = cmatrix[row_j], cmatrix[row_i]
    return cmatrix

def simplify_matrix(matrix):
    B = deepcopy(matrix)
    i = 0
    while i < len(B):
        f = leading_term_index(B[i])
        if f < 0:
            i += 1
            continue
        B = row_op_mult(B, i, 1 / B[i][f])
        i += 1
    return B

def rref(matrix):
    return gaussian_elimination(matrix, reduced=True)

def ref(matrix):
    return gaussian_elimination(matrix, reduced=False)

def gaussian_elimination(matrix, reduced=True):
    B = deepcopy(matrix)
    i = 0
    while i < len(B):
        f = leading_term_index(B[i])
        if f < 0:
            i += 1
            continue
        B = row_op_mult(B, i, 1 / B[i][f])
        j = 0 if reduced else i + 1
        while j < len(B):
            if j == i:
                j += 1
                continue
            s = 1 if B[i][f] < 0 == B[j][f] < 0 else -1
            B = row_op_add(B, i, j, s * B[j][f] / B[i][f])
            if is_zero_vector(B[j]):
                for h in range(j + 1, len(B)):
                    B = row_op_swap(B, h - 1, h)
            j += 1
        i += 1
    return B

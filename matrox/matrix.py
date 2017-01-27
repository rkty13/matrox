from copy import deepcopy
import numbers

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

def zero_matrix(rows, cols):
    return Matrix([[j for j in range(cols)] for i in range(rows)])

def num_rows(matrix):
    return len(matrix)

def num_cols(matrix):
    return len(matrix[0])

def scalar_mult_matrix(matrix, k):
    matrix_c = zero_matrix(num_rows(matrix), num_cols(matrix))
    for m in range(num_rows(matrix)):
        for n in range(num_cols(matrix)):
            matrix_c[m][n] = matrix[m][n] * k
    return matrix_c

def add_matrices(matrix_a, matrix_b):
    matrix_c = zero_matrix(num_rows(matrix_a), num_cols(matrix_a))
    for m in range(num_rows(matrix_c)):
        for n in range(num_cols(matrix_c)):
            matrix_c[m][n] = matrix_a[m][n] + matrix_b[m][n]
    return matrix_c

def subtract_matrices(matrix_a, matrix_b):
    negated = scalar_mult_matrix(matrix_b, -1)
    return add_matrices(matrix_a, negated)

def multiply_matrices(matrix_a, matrix_b):
    if isinstance(matrix_a, numbers.Number):
        return scalar_mult_matrix(matrix_b, matrix_a)
    if isinstance(matrix_b, numbers.Number):
        return scalar_mult_matrix(matrix_a, matrix_b)
    matrix_c = zero_matrix(num_rows(matrix_a), num_cols(matrix_b))
    for i in range(num_rows(matrix_a)):
        for j in range(num_cols(matrix_b)):
            el_sum = 0
            for k in range(num_cols(matrix_a)):
                el_sum += matrix_a[i][k] * matrix_b[k][j]
            matrix_c[i][j] = el_sum
    return matrix_c

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

from copy import deepcopy

from matrox import identity_matrix, num_rows

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

def el_matrix_add(matrix, i, j, k):
    t = identity_matrix(num_rows(matrix))
    t[i][j] = deepcopy(k)
    return t

def el_matrix_mult(matrix, i, k):
    t = identity_matrix(num_rows(matrix))
    t[i][i] = deepcopy(k)
    return t

def el_matrix_swap(matrix, i, j):
    t = identity_matrix(num_rows(matrix))
    t[i], t[j] = t[j], t[i]
    return t

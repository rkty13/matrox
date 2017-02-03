from copy import deepcopy

from matrox import identity_matrix, num_rows

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
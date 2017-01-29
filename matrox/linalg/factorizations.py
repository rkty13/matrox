from copy import deepcopy

from matrox import (
    assert_square_matrix,
    identity_matrix,
    is_symmetric,
    num_rows,
    row_op_add,
    row_op_mult,
    el_matrix_swap
)

@assert_square_matrix
def permute_matrix(matrix):
    permuted = identity_matrix(num_rows(matrix))
    permute_from = deepcopy(matrix)
    for i in range(num_rows(permute_from)):
        if permute_from[i][i] == 0:
            s = i + 1
            while s < num_rows(permute_from):
                if permute_from[s][i] != 0:
                    break
                else:
                    s += 1
            if s < num_rows(permute_from):
                permuted = el_matrix_swap(permuted, i, s)
                permute_from = el_matrix_swap(permute_from, i, s)
    return permuted

@assert_square_matrix
def upper_triangular(matrix, history=False, inverse_history=False):
    matrix_c = deepcopy(matrix)
    traceback = []
    inverse_traceback = []
    i = 0
    while i < num_rows(matrix):
        j = i + 1
        while j < num_rows(matrix):
            if j == i:
                j += 1
                continue
            s = 1 if matrix_c[i][i] < 0 == matrix_c[j][i] < 0 else -1
            m = s * matrix_c[j][i] / matrix_c[i][i]
            matrix_c = row_op_add(matrix_c, i, j, m)
            if history:
                t = identity_matrix(num_rows(matrix))
                t[j][i] = deepcopy(m)
                traceback.append(t)
            if inverse_history:
                t = identity_matrix(num_rows(matrix))
                t[j][i] = deepcopy(-m)
                inverse_traceback.append(t)
            j += 1
        i += 1
    return matrix_c, traceback, inverse_traceback

@assert_square_matrix
def lower_triangular(matrix, history = False, inverse_history = False):
    matrix_c = deepcopy(matrix)
    traceback = []
    inverse_traceback = []
    i = num_rows(matrix_c) - 1
    while i >= 0:
        j = i - 1
        while j >= 0:
            if j == i:
                j -= 1
                continue
            s = 1 if matrix_c[i][i] < 0 == matrix_c[j][i] < 0 else -1
            m = s * matrix_c[j][i] / matrix_c[i][i]
            matrix_c = row_op_add(matrix_c, i, j, m)
            if history:
                t = identity_matrix(num_rows(matrix))
                t[j][i] = deepcopy(m)
                traceback.append(t)
            if inverse_history:
                t = identity_matrix(num_rows(matrix))
                t[j][i] = deepcopy(-m)
                inverse_traceback.append(t)
            j -= 1
        i -= 1
    return matrix_c, traceback, inverse_traceback

@assert_square_matrix
def lu_factorization(matrix):
    upper_pieces = upper_triangular(matrix, inverse_history=True)
    upper = upper_pieces[0]
    lower = identity_matrix(num_rows(matrix))
    for i in range(len(upper_pieces[2])):
        lower = lower * upper_pieces[2][i]
    return lower, upper

@assert_square_matrix
def ldu_factorization(matrix):
    lower, upper = lu_factorization(matrix)
    diagonal = identity_matrix(num_rows(matrix))
    for i in range(num_rows(diagonal)):
        diagonal[i][i] = deepcopy(upper[i][i])
        upper = row_op_mult(upper, i, 1 / upper[i][i])
    return lower, diagonal, upper

@assert_square_matrix
def plu_factorization(matrix):
    permuted = permute_matrix(matrix)
    lower, upper = lu_factorization(permuted * matrix)
    return permuted, lower, upper

@assert_square_matrix
def ldlt_factorization(matrix):
    if not is_symmetric(matrix):
        return None, None, None
    return ldu_factorization(matrix)

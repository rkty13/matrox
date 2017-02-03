from copy import deepcopy

from matrox import (
    dim,
    identity_matrix,
    is_zero_vector,
    leading_term_index,
    num_rows,
    row_op_add,
    row_op_mult,
    row_op_swap
)

from . import el_matrix_add, el_matrix_mult, el_matrix_swap

def rref(matrix, history=False, inverse_history=False):
    return gaussian_elimination(matrix, reduced=True, history=history,
        inverse_history=inverse_history)

def ref(matrix, history=False, inverse_history=False):
    return gaussian_elimination(matrix, reduced=False, history=history,
        inverse_history=inverse_history)

def gaussian_elimination(matrix, reduced=True, history=False,
        inverse_history=False):
    matrix_c = deepcopy(matrix)
    traceback = []
    inverse_traceback = []
    i = 0
    while i < num_rows(matrix_c):
        lead = leading_term_index(matrix_c[i])
        if lead < 0:
            i += 1
            continue
        r = 1 / matrix_c[i][lead]
        matrix_c = row_op_mult(matrix_c, i, r)
        if history:
            traceback.append(el_matrix_mult(matrix_c, i, r))
        if inverse_history:
            inverse_traceback.append(el_matrix_mult(matrix_c, i, 1 / r))
        j = 0 if reduced else i + 1
        while j < num_rows(matrix_c):
            if j == i:
                j += 1
                continue
            sign = 1 if matrix_c[i][lead] < 0 == matrix_c[j][lead] < 0 else -1
            m = sign * matrix_c[j][lead] / matrix_c[i][lead]
            matrix_c = row_op_add(matrix_c, i, j, m)
            if history:
                traceback.append(el_matrix_add(matrix_c, j, i, m))
            if inverse_history:
                inverse_traceback.append(el_matrix_add(matrix_c, j, i, -m))
            j += 1
        i += 1
    for j in range(num_rows(matrix_c)):
        if is_zero_vector(matrix_c[j]):
            for h in range(j + 1, num_rows(matrix_c)):
                matrix_c = row_op_swap(matrix_c, h - 1, h)
                if history:
                    traceback.append(el_matrix_swap(matrix_c, h - 1, h))
                if inverse_history:
                    inverse_traceback.append(
                        el_matrix_swap(matrix_c, h - 1, h))
    return matrix_c, traceback, inverse_traceback

from copy import deepcopy

from matrox import (
    leading_term_index,
    zero_matrix,
    num_rows,
    num_cols,
    Matrix
)

from . import rref

def null_basis(matrix):
    U = rref(matrix)[0]
    pivots = set()
    for i in range(num_rows(U)):
        pivot = leading_term_index(U[i])
        if pivot != -1:
            pivots.add(pivot)
    free = { i for i in range(num_rows(U)) } - pivots
    if len(free) == 0:
        return []

def back_substitution(U, x, b):
    x_n = deepcopy(x)
    for i in range(num_rows(U) - 1, -1, -1):
        pivot = leading_term_index(U[i])
        if pivot != -1:
            x_n[pivot][0] = (b[i][0] - sum([x_n[j][0] * U[i][j] for j in range(num_rows(x_n))])) / U[i][pivot]
    return x_n

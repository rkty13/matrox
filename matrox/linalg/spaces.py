from copy import deepcopy

from matrox import (
    leading_term_index,
    num_rows,
    num_cols,
    zero_matrix
)

from . import rref

def null_basis(matrix):
    U = rref(matrix)[0]
    b = zero_matrix(num_rows(U), 1)
    solutions = []
    pivots = set()
    for i in range(num_rows(U)):
        pivot = leading_term_index(U[i])
        if pivot != -1:
            pivots.add(pivot)
    free = { i for i in range(num_cols(U)) } - pivots
    if len(free) == 0:
        return solutions
    for i in free:
        x = zero_matrix(num_cols(U), 1)
        x[i][0] = 1
        solutions.append(back_substitution(U, x, b))
    return solutions

def back_substitution(U, x, b):
    x_n = deepcopy(x)
    for i in range(num_rows(U) - 1, -1, -1):
        pivot = leading_term_index(U[i])
        if pivot != -1:
            x_n[pivot][0] = (
                    b[i][0] - 
                    sum([x_n[j][0] * U[i][j] for j in range(num_rows(x_n))]) \
                ) / U[i][pivot]
    return x_n

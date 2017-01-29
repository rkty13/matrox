from copy import deepcopy

from matrox import (
    leading_term_index,
    row_op_mult,
    row_op_add,
    row_op_swap,
    is_zero_vector,
    num_rows
)

def rref(matrix):
    return gaussian_elimination(matrix, reduced=True)

def ref(matrix):
    return gaussian_elimination(matrix, reduced=False)

def gaussian_elimination(matrix, reduced=True):
    B = deepcopy(matrix)
    i = 0
    while i < num_rows(B):
        f = leading_term_index(B[i])
        if f < 0:
            i += 1
            continue
        B = row_op_mult(B, i, 1 / B[i][f])
        j = 0 if reduced else i + 1
        while j < num_rows(B):
            if j == i:
                j += 1
                continue
            s = 1 if B[i][f] < 0 == B[j][f] < 0 else -1
            B = row_op_add(B, i, j, s * B[j][f] / B[i][f])
            if is_zero_vector(B[j]):
                for h in range(j + 1, num_rows(B)):
                    B = row_op_swap(B, h - 1, h)
            j += 1
        i += 1
    return B

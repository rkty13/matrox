from . import (
    gaussian_elimination,
    ref
)

from matrox import (
    assert_square_matrix,
    identity_matrix,
    is_identity,
    num_non_zero_rows,
    num_rows
)

def rank(matrix):
    reduced = ref(matrix)
    return num_non_zero_rows(reduced[0])

@assert_square_matrix
def inverse(matrix):
    reduced, traceback, _ = gaussian_elimination(matrix, history=True)
    inverted = identity_matrix(num_rows(matrix))
    if is_identity(reduced):
        for el in traceback:
            inverted = el * inverted
        return inverted
    else:
        return None
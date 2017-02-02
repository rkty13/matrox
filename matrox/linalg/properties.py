from . import ref

from matrox import num_non_zero_rows

def rank(matrix):
    reduced = ref(matrix)
    return num_non_zero_rows(reduced[0])
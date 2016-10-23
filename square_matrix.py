from matrix import Matrix
from exceptions import DimensionError

class SquareMatrix(Matrix):
    def __init__(self, size = 0, copy = None, fractional = True):
        if copy and copy.num_rows() != copy.num_cols():
            raise DimensionError("Square matrices must have n x n dimensions.")
        super().__init__(rows = size, cols = size, copy = copy, fractional = fractional)

    def determinant(self):
        pass

    def inverse(self):
        pass
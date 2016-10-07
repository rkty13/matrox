from exceptions import DimensionError
from matrix import Matrix

a = Matrix(copy = [[2, 3], [4, 5]])
b = Matrix(copy = [[4, 2], [1, 2]])

print("a: ", a)
print("b: ", b)
print("a + b: ", a + b)
print("a - b: ", a - b)
print("b - a: ", b - a)
print("transpose(a): ", a.transpose())

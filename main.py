from exceptions import DimensionError
from matrix import Matrix
from vector import Vector

a = Matrix(copy = [[2, 3], [4, 5]])
b = Matrix(copy = [[4, 2], [1, 2]])

print("a: ", a)
print("b: ", b)
print("a + b: ", a + b)
print("a - b: ", a - b)
print("b - a: ", b - a)
print("a * b: ", a * b)
print("b * a: ", b * a)
print("a ** 2: ", a ** 2)
print("transpose(a): ", a.transpose())
a += b
print("a += b: ", a)
a -= b
print("a -= b: ", a)
a *= b
print("a *= b: ", a)

u = Vector(copy = [1, 2, 3, 4])
v = Vector(copy = [3, 2, 4, 1])

print("u: ", u)
print("v: ", v)
print("u + v: ", u + v)
print("u - v: ", u - v)
print("v - u: ", v - u)
print("u * v: ", u * v)
print("v * u: ", v * u)
u += v
print("u += v: ", u)
u -= v
print("u -= v: ", u)
u *= v
print("u *= v: ", u)
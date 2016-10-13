from exceptions import DimensionError
from matrix import Matrix
from vector import Vector

print("\nBASIC MATRIX ARITHMETIC")

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
print("transpose(b): ", b.transpose())
a += b
print("a += b: ", a)
a -= b
print("a -= b: ", a)
a *= b
print("a *= b: ", a)

print("\nGAUSS-JORDAN ELIMINATION")

c = Matrix(copy = [[2, 3, 4], [4, 5, 2]])
d = Matrix(copy = [[4, 2, 1], [1, 2, 10]])
print("c: ", c)
print("d: ", d)
print("GJE c: ", c.gauss_jordan_elimination())
print("GJE d: ", d.gauss_jordan_elimination())

print("\nBASIC VECTOR ARITHMETIC")

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


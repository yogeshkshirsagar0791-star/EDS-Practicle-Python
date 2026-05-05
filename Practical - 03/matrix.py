import numpy as np

a = np.array([[2, 3],[4, 5]])
b = np.array([[6, 7],[8, 9]])

print("matrix1 = \n", a)
print("matrix2 = \n", b)

print("\n addition of matrices:")
print(np.add(a,b))

print("\n subtraction of matrices: ")
print(np.subtract(a,b))

print("\n matrix division: ")
print(np.divide(a,b))

print("\n Multiplication of matrices: ")
print(np.multiply(a,b))
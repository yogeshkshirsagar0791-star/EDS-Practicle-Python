import numpy as np

a = np.array([[4, 5],[6, 7]])
b = np.array([[8, 9],[10, 11]])

print("matrix1 = \n", a)
print("matrix2 = \n", b)

print("\n addition:")
print(np.add(a,b))

print("\n subtraction : ")
print(np.subtract(a,b))

print("\n division: ")
print(np.divide(a,b))

print("\n matrices: ")
print(np.multiply(a,b))

print("\n The sum of elements=")
print(np.sum(a))

print("\n The column wise sum=")
print(np.sum(a,axis=0))

print("\n The row wise sum=")
print(np.sum(a,axis=1))

print("\nThe transpose= ")
print(a.T)
import numpy as np

a = np.array([6, 7, 8])
b = np.array([2, 3, 4])

corr_a = np.corrcoef(a, b)
print(corr_a)
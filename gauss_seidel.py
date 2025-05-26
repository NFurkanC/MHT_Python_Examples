import numpy as np

max_iter = 25

A = np.array([[10, -1 , 2], [6, 2, 5], [2, -1, 10]])
b = np.array([6, 25, -11])
x = np.zeros_like(b)

for _ in range(max_iter):
    for i in range(len(A)):
        s1 = sum(A[i][j] * x[j] for j in range(i))
        s2 = sum(A[i][j] * x[j] for j in range(i + 1, len(A)))
        x[i] = (b[i] - s1 - s2) / A[i][i]

print("Result: ", x)    
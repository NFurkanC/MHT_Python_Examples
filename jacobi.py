import numpy as np

max_iter = 25

A = np.array([[10, -1 , 2], [6, 2, 5], [2, -1, 10]])
b = np.array([6, 25, -11])
x = np.zeros_like(b)

for _ in range(max_iter):
    x_n = np.zeros_like(x)
    for i in range(len(A)):
        s = sum(A[i][j] * x[j] for j in range(len(A)) if i != j)
        x_n[i] = (b[i] - s) / A[i][i]
    x = x_n.copy()

print("Result: ", x)
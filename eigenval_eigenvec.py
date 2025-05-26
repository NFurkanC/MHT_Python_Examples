import numpy as np

A = np.array([[4, -2], [1, 1]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Özdeğerler:", eigenvalues)
print("Özvektörler:", eigenvectors)

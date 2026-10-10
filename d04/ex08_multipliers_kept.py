"""The multipliers are not waste: kept in the zeros they create, they are half the
factorisation."""
import numpy as np

A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
M = np.array(A, copy=True)

for k in range(2):
    for i in range(k + 1, 3):
        m = M[i, k] / M[k, k]
        M[i, k + 1:] -= m * M[k, k + 1:]
        M[i, k] = m                       # written where the zero would have gone
print("one array holding both triangles:\n", np.array2string(M, precision=4))
L = np.tril(M, -1) + np.eye(3)
U = np.triu(M)
print("\nL @ U:\n", np.array2string(L @ U, precision=4))
print("\nthe original A:\n", A)

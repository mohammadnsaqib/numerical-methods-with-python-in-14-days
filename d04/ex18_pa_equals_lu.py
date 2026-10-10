"""The whole factorisation in one identity: the permuted matrix equals L times U."""
import numpy as np

from nmkit.linsolve import lu_pivot

A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
LU, piv, _ = lu_pivot(A)
L = np.tril(LU, -1) + np.eye(3)
U = np.triu(LU)
P = np.eye(3)[piv, :]

print("L =\n", np.array2string(L, precision=6))
print("U =\n", np.array2string(U, precision=6))
print("P A =\n", np.array2string(P @ A, precision=6))
print("L U =\n", np.array2string(L @ U, precision=6))
print("largest difference:", f"{np.max(np.abs(P @ A - L @ U)):.3e}")

"""Removing one eigenpair leaves the others untouched, so the method can be run again.
"""
import numpy as np

from nmkit.eigen import deflate, power_method

A = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
print("true eigenvalues:", np.array2string(np.linalg.eigvalsh(A), precision=10))

M = A.copy()
for step in range(3):
    lam, v, _, _ = power_method(M, tol=1e-13, max_iter=5000)
    print(f"  found {lam:>13.10f}")
    M = deflate(M, lam, v)

"""Shifting and inverting turns the eigenvalue nearest a guess into the largest one."""
import numpy as np

from nmkit.eigen import inverse_iteration, residual

A = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
print("all eigenvalues:", np.array2string(np.linalg.eigvalsh(A), precision=10))

for shift in (1.0, 3.0, 5.0):
    lam, v, k, _ = inverse_iteration(A, shift, tol=1e-13)
    print(f"shift {shift}: found {lam:.12f} in {k:>2} steps, residual "
          f"{residual(A, lam, v):.2e}")

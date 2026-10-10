"""Problem 4.38: how the error without pivoting grows as the first pivot shrinks."""
import numpy as np

from nmkit.linsolve import gauss_naive, solve

print(f"{'first pivot':>13} {'no pivoting':>14} {'with pivoting':>15}")
for p in (1e-2, 1e-6, 1e-10, 1e-14, 1e-18):
    A = np.array([[p, 1.0], [1.0, 1.0]])
    b = np.array([1.0, 2.0])
    true = np.linalg.solve(A, b)
    e_naive = np.max(np.abs(gauss_naive(A, b) - true))
    e_piv = np.max(np.abs(solve(A, b) - true))
    print(f"{p:>13.0e} {e_naive:>14.3e} {e_piv:>15.3e}")

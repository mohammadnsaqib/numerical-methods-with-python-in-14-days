"""Elimination fills in the zeros, so a sparse matrix stops being sparse halfway
through."""
import numpy as np

from nmkit.linsolve import lu_pivot

n = 12
A = (np.diag(4.0 * np.ones(n)) + np.diag(-1.0 * np.ones(n - 1), 1)
     + np.diag(-1.0 * np.ones(n - 1), -1) + np.diag(-1.0 * np.ones(n - 4), 4)
     + np.diag(-1.0 * np.ones(n - 4), -4))

LU, _, _ = lu_pivot(A)
print("nonzero entries in A :", int(np.count_nonzero(A)))
print("nonzero entries in LU:", int(np.count_nonzero(np.abs(LU) > 1e-14)))
print("entries in the whole matrix:", n * n)
print("the factorisation "
      "is", f"{np.count_nonzero(np.abs(LU) > 1e-14) / np.count_nonzero(A):.2f}",
      "times as full as A")

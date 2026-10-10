"""A pivot that is merely small stops nothing and destroys the answer in silence."""
import numpy as np

from nmkit.linsolve import gauss_naive, residual, solve

eps = 1e-18
A = np.array([[eps, 1.0], [1.0, 1.0]])
b = np.array([1.0, 2.0])

naive = gauss_naive(A, b)
piv = solve(A, b)
true = np.linalg.solve(A, b)
print("no pivoting  :", np.array2string(naive, precision=17))
print("with pivoting:", np.array2string(piv, precision=17))
print("numpy        :", np.array2string(true, precision=17))
print("error, no pivoting  :", f"{np.max(np.abs(naive - true)):.3e}")
print("error, with pivoting:", f"{np.max(np.abs(piv - true)):.3e}")

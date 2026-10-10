"""The routine is checked by rebuilding the matrix, and against an independent
implementation."""
import numpy as np
from scipy.linalg import cholesky as sp_cholesky

from nmkit.factor import cholesky

rng = np.random.default_rng(71)
n = 6
B = rng.normal(size=(n, n))
A = B @ B.T + n * np.eye(n)  # symmetric and positive definite by construction

L = cholesky(A)
print("largest entry of L @ L.T minus A:", f"{np.max(np.abs(L @ L.T - A)):.3e}")
print("largest gap from scipy's L      :",
      f"{np.max(np.abs(L - sp_cholesky(A, lower=True))):.3e}")
print("L is lower triangular           :", np.allclose(L, np.tril(L)))

"""The factorisation is checked by rebuilding the matrix it came from."""
import numpy as np

from nmkit.linsolve import lu_pivot

rng = np.random.default_rng(5)
A = rng.uniform(-4, 4, (5, 5))
LU, piv, swaps = lu_pivot(A)
L = np.tril(LU, -1) + np.eye(5)
U = np.triu(LU)

print("row order:", piv)
print("largest entry of L @ U minus the permuted A:",
      f"{np.max(np.abs(L @ U - A[piv, :])):.3e}")
print("largest multiplier:", f"{np.max(np.abs(np.tril(LU, -1))):.6f}")

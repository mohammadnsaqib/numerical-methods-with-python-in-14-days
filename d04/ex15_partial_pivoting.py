"""Partial pivoting chooses the largest entry in the column, so no multiplier ever
exceeds one."""
import numpy as np

from nmkit.linsolve import lu_pivot

A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
LU, piv, swaps = lu_pivot(A)
mult = np.tril(LU, -1)

print("row order chosen:", piv, " exchanges:", swaps)
print("the multipliers:\n", np.array2string(mult, precision=6))
print("largest multiplier in size:", f"{np.max(np.abs(mult)):.6f}")
print("every one is at or below 1:", np.all(np.abs(mult) <= 1.0))

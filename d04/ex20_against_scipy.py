"""Two libraries factor the same matrix and their U agrees entry for entry."""
import numpy as np
from scipy.linalg import lu_factor

from nmkit.linsolve import lu_pivot

rng = np.random.default_rng(23)
A = rng.uniform(-3, 3, (6, 6))

mine, piv, _ = lu_pivot(A)
theirs, ipiv = lu_factor(A)

# SciPy reports the pivoting as a sequence of row exchanges rather than as a final row
# order, so the two have to be put in the same form before they can be compared at all.
order = np.arange(6)
for k, p in enumerate(ipiv):
    order[[k, p]] = order[[p, k]]

print("largest gap in U:", f"{np.max(np.abs(np.triu(mine) - np.triu(theirs))):.3e}")
print("largest "
      "gap in L:", f"{np.max(np.abs(np.tril(mine, -1) - np.tril(theirs, -1))):.3e}")
print("nmkit row order :", piv)
print("scipy row order :", order)
print("they agree      :", np.array_equal(piv, order))

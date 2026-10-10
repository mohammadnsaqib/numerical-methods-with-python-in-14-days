"""The routine does what the three hand lines did, for any size, and its answer is
checkable."""
import numpy as np

from nmkit.linsolve import back_sub

rng = np.random.default_rng(3)
n = 6
U = np.triu(rng.uniform(-3, 3, (n, n)))
U[np.diag_indices(n)] += 4.0                    # keep the diagonal away from zero
x_true = np.arange(1.0, n + 1.0)
b = U @ x_true

x = back_sub(U, b)
print("recovered x :", np.array2string(x, precision=12))
print("true x      :", x_true)
print("largest gap :", f"{np.max(np.abs(x - x_true)):.3e}")

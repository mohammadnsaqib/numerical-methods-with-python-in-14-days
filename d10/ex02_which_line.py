"""Among all the lines that miss, one misses by the least in the sum of squares."""
import numpy as np

from nmkit.lstsq import lstsq_qr, residual

A = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])
b = np.array([1.0, 3.0, 2.0])
x = lstsq_qr(A, b)

print("the least squares line:", np.array2string(x, precision=12))
print("its sum of squares    :", f"{float(residual(A, x, b) @ residual(A, x, b)):.12f}")
rng = np.random.default_rng(197)
worse = 0
for _ in range(20000):
    y = x + rng.normal(scale=0.3, size=2)
    r = residual(A, y, b)
    if r @ r < residual(A, x, b) @ residual(A, x, b) - 1e-12:
        worse += 1
print("nearby lines that beat it, out of 20000:", worse)

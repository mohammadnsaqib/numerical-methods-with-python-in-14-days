"""What singles the least-squares fit out: its residual is at right angles to every
column."""
import numpy as np

from nmkit.lstsq import lstsq_qr, residual

rng = np.random.default_rng(199)
A = rng.normal(size=(20, 4))
b = rng.normal(size=20)
x = lstsq_qr(A, b)
r = residual(A, x, b)

print("residual against each column of A:")
for j in range(4):
    print(f"  column {j}: {float(A[:, j] @ r):+.3e}")
print("a wrong answer does not have this property:")
bad = x + np.array([0.1, 0.0, 0.0, 0.0])
print(f"  column 0 with a shifted fit: {float(A[:, 0] @ residual(A, bad, b)):+.6f}")

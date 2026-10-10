"""Squaring the residuals is a choice, and it is the one that gives a linear system."""
import numpy as np

from nmkit.lstsq import lstsq_qr, residual

A = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0], [1.0, 3.0]])
b = np.array([1.0, 3.0, 2.0, 9.0])                    # the last point is an outlier

sq = lstsq_qr(A, b)
# The sum of ABSOLUTE residuals has no closed form, so it is searched for on a grid.
best, best_val = None, 1e18
for c0 in np.linspace(-2, 4, 601):
    for c1 in np.linspace(-1, 4, 501):
        v = float(np.sum(np.abs(b - A @ np.array([c0, c1]))))
        if v < best_val:
            best, best_val = np.array([c0, c1]), v

print("least SQUARES  :", np.array2string(sq, precision=6))
print("least ABSOLUTE :", np.array2string(best, precision=6))
print("outlier residual:", f"squares {abs(b[3] - A[3] @ sq):.2f}",
      f"absolute {abs(b[3] - A[3] @ best):.2f}")
print("only the squares criterion is minimised by solving a linear system.")

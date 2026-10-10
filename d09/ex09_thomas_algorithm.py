"""One forward pass and one backward pass, and the cost grows with n rather than n
cubed."""
import numpy as np

from nmkit.spline import thomas

n = 6
lower = np.full(n - 1, 1.0)
diag = np.full(n, 4.0)
upper = np.full(n - 1, 1.0)
rhs = np.arange(1.0, n + 1.0)

x = thomas(lower, diag, upper, rhs)
A = np.diag(diag) + np.diag(lower, -1) + np.diag(upper, 1)
print("Thomas         :", np.array2string(x, precision=12))
print("full elimination:", np.array2string(np.linalg.solve(A, rhs), precision=12))
print("largest gap    :", f"{np.max(np.abs(x - np.linalg.solve(A, rhs))):.3e}")

"""Three points on no straight line: the system has more equations than unknowns and no
answer."""
import numpy as np

A = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])     # a line: intercept and slope
b = np.array([1.0, 3.0, 2.0])

print("A is", A.shape[0], "by", A.shape[1], "-- more equations than unknowns")
try:
    np.linalg.solve(A, b)
except Exception as exc:
    print("an exact solve refuses:", type(exc).__name__)
for x in ([1.0, 1.0], [1.5, 0.5], [2.0, 0.0]):
    r = b - A @ np.array(x)
    print(f"  x = {x}: residual {np.array2string(r, precision=4)}  "
          f"sum of squares {float(r @ r):.4f}")

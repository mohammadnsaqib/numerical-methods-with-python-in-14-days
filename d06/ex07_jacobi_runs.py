"""The routine collects the hand sweeps and reports how many it needed."""
import numpy as np

from nmkit.iterative import jacobi

A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 4.0]])
b = np.array([2.0, 4.0, 10.0])

x, k, hist = jacobi(A, b, tol=1e-12)
print("answer      :", np.array2string(x, precision=12))
print("direct solve:", np.array2string(np.linalg.solve(A, b), precision=12))
print("sweeps      :", k)
print("largest gap :", f"{np.max(np.abs(x - np.linalg.solve(A, b))):.3e}")

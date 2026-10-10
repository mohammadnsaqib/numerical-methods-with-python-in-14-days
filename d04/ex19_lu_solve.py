"""One factorisation answers many right-hand sides, which is the reason to keep it."""
import numpy as np

from nmkit.linsolve import lu_pivot, lu_solve, residual

A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
LU, piv, _ = lu_pivot(A)

for b in (np.array([8.0, -11.0, -3.0]),
          np.array([1.0, 0.0, 0.0]),
          np.array([0.0, 5.0, 5.0])):
    x = lu_solve(LU, piv, b)
    print(f"b = {b}  ->  x = {np.array2string(x, precision=8)}  "
          f"residual {np.linalg.norm(residual(A, x, b)):.2e}")

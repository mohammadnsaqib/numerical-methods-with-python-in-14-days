"""An iterative method touches only the entries that are there, so size stops being the
problem."""
import numpy as np

from nmkit.iterative import gauss_seidel

n = 400
A = (np.diag(4.0 * np.ones(n)) + np.diag(-1.0 * np.ones(n - 1), 1)
     + np.diag(-1.0 * np.ones(n - 1), -1))
b = np.ones(n)

x, k, _ = gauss_seidel(A, b, tol=1e-10, max_iter=2000)
print("size          :", n)
print("sweeps needed :", k)
print("largest residual:", f"{np.max(np.abs(b - A @ x)):.3e}")
print("gap from a direct solve:", f"{np.max(np.abs(x - np.linalg.solve(A, b))):.3e}")

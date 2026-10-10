"""Pushing the correction past its target can reach the answer in far fewer sweeps."""
import numpy as np

from nmkit.iterative import sor

n = 20
A = (np.diag(4.0 * np.ones(n)) + np.diag(-1.0 * np.ones(n - 1), 1)
     + np.diag(-1.0 * np.ones(n - 1), -1))
b = np.ones(n)

for w in (0.8, 1.0, 1.2, 1.4, 1.6):
    _, k, _ = sor(A, b, omega=w, tol=1e-10, max_iter=2000)
    marker = "   (this is Gauss-Seidel)" if w == 1.0 else ""
    print(f"omega {w:.1f}: {k:>4} sweeps{marker}")

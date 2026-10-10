"""When the two largest are nearly equal the method barely moves, however long it runs.
"""
import numpy as np

from nmkit.eigen import power_method

for gap in (0.5, 0.1, 0.01, 0.001):
    A = np.diag([1.0, 1.0 - gap, 0.1])
    lam, _, k, _ = power_method(A, x0=np.array([1.0, 1.0, 1.0]), tol=1e-12,
                                max_iter=20000)
    print(f"gap {gap:<6}: {k:>6} iterations, eigenvalue {lam:.10f}")

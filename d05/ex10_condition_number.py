"""The condition number is computable, and it is a property of the matrix alone."""
import numpy as np

from nmkit.norms import cond, hilbert

cases = [
    ("identity   ", np.eye(4)),
    ("well scaled", np.array([[2.0, 1.0], [1.0, 3.0]])),
    ("badly scaled", np.array([[1.0, 0.0], [0.0, 1e-8]])),
    ("Hilbert 6  ", hilbert(6)),
]
for name, A in cases:
    print(f"{name}: cond {cond(A, 2):>12.4e}   numpy {np.linalg.cond(A, 2):>12.4e}")

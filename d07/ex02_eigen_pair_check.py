"""A claimed eigenpair is checked by a residual, exactly as a root or a linear solve is.
"""
import numpy as np

from nmkit.eigen import residual

A = np.array([[3.0, 1.0], [1.0, 3.0]])
for lam, v in ((4.0, np.array([1.0, 1.0]) / np.sqrt(2)),
               (2.0, np.array([1.0, -1.0]) / np.sqrt(2)),
               (3.5, np.array([1.0, 1.0]) / np.sqrt(2))):
    print(f"lambda {lam}: residual {residual(A, lam, v):.3e}")
print("\nthe third pair has the right direction and the wrong stretch.")

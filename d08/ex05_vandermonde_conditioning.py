"""The matrix is badly conditioned, and it gets worse quickly with the count of points.
"""
import numpy as np

from nmkit.norms import cond
from nmkit.interp import vandermonde_matrix

print(f"{'points':>8} {'condition number':>20} {'digits lost':>13}")
for n in (3, 5, 8, 12, 16, 20):
    xs = np.linspace(-1.0, 1.0, n)
    k = cond(vandermonde_matrix(xs), 2)
    print(f"{n:>8} {k:>20.4e} {np.log10(k):>13.2f}")

"""Adding points adds PIECES, not degree, so nothing has room to oscillate."""
import numpy as np

for n in (5, 10, 50, 500, 5000):
    print(f"{n:>6} points: one polynomial has degree {n - 1:>4}, "
          f"a cubic spline has {n - 1:>4} pieces of degree 3")

"""The one number that decides convergence, computed for four matrices."""
import numpy as np

from nmkit.iterative import (diagonally_dominant, iteration_matrix, spectral_radius)

cases = [
    ("diagonally dominant", np.array([[4.0, -1.0], [-1.0, 4.0]])),
    ("barely dominant    ", np.array([[2.0, -1.9], [-1.9, 2.0]])),
    ("not dominant       ", np.array([[1.0, 2.0], [2.0, 1.0]])),
    ("badly ordered      ", np.array([[1.0, 4.0], [4.0, 1.0]])),
]
for name, A in cases:
    r = spectral_radius(iteration_matrix(A, "jacobi"))
    print(f"{name}: radius {r:>8.4f}   converges: {str(r < 1):<5}  "
          f"dominant: {diagonally_dominant(A)}")

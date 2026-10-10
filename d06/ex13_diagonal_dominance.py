"""Diagonal dominance guarantees convergence, and its absence guarantees nothing either
way."""
import numpy as np

from nmkit.iterative import diagonally_dominant, iteration_matrix, spectral_radius

cases = [
    ("dominant, "
     "converges    ", np.array([[5.0, 1.0, 1.0], [1.0, 5.0, 1.0], [1.0, 1.0, 5.0]])),
    ("not dominant, "
     "converges", np.array([[4.0, 5.0, 0.0], [0.0, 4.0, 1.0], [1.0, 0.0, 4.0]])),
    ("not dominant, "
     "diverges ", np.array([[1.0, 2.0, 2.0], [2.0, 1.0, 2.0], [2.0, 2.0, 1.0]])),
]
for name, A in cases:
    print(f"{name}: dominant {str(diagonally_dominant(A)):<5}  "
          f"radius {spectral_radius(iteration_matrix(A, 'jacobi')):.4f}")
print("\ndominance is sufficient and not necessary: the middle row proves it.")

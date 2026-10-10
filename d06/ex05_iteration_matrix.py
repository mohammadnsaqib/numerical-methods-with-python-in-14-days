"""The error is multiplied by one fixed matrix at every sweep, and that matrix can be
written down."""
import numpy as np

from nmkit.iterative import iteration_matrix, spectral_radius

A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 4.0]])
for name in ("jacobi", "gauss_seidel"):
    M = iteration_matrix(A, name)
    print(f"{name:>13}: spectral radius {spectral_radius(M):.6f}")
    print(f"{'':>13}  eigenvalues {np.round(np.abs(np.linalg.eigvals(M)), 6)}")

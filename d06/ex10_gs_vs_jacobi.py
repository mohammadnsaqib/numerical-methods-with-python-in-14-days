"""The same problem, the same tolerance, and about half the sweeps."""
import numpy as np

from nmkit.iterative import gauss_seidel, iteration_matrix, jacobi, spectral_radius

A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 4.0]])
b = np.array([2.0, 4.0, 10.0])

_, kj, _ = jacobi(A, b, tol=1e-12)
_, kg, _ = gauss_seidel(A, b, tol=1e-12)
rj = spectral_radius(iteration_matrix(A, "jacobi"))
rg = spectral_radius(iteration_matrix(A, "gauss_seidel"))
print(f"Jacobi      : {kj:>3} sweeps, spectral radius {rj:.6f}")
print(f"Gauss-Seidel: {kg:>3} sweeps, spectral radius {rg:.6f}")
print(f"the radius is squared: {rj ** 2:.6f}")

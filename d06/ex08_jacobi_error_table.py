"""The step falls by the spectral radius, but only when measured over a whole cycle."""
import numpy as np

from nmkit.iterative import iteration_matrix, jacobi, spectral_radius

A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 4.0]])
b = np.array([2.0, 4.0, 10.0])
_, _, hist = jacobi(A, b, tol=1e-14)

print(f"{'sweep':>6} {'step':>14} {'one sweep':>11} {'two sweeps':>12}")
for k in range(2, 10):
    two = np.sqrt(hist[k] / hist[k - 2])
    print(f"{k:>6} {hist[k]:>14.4e} {hist[k] / hist[k - 1]:>11.6f} {two:>12.6f}")

rho = spectral_radius(iteration_matrix(A, "jacobi"))
print(f"\nspectral radius: {rho:.6f}")
print("the one-sweep ratio alternates because the largest entry of the error moves")
print("between components; over two sweeps it settles on the radius itself.")

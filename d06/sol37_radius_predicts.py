"""Problem 6.37: the sweeps a method needs, predicted from its spectral radius alone."""
import numpy as np

from nmkit.iterative import (gauss_seidel, iteration_matrix, jacobi, spectral_radius)

print(f"{'size':>6} {'method':>14} {'radius':>9} {'predicted':>11} {'actual':>8}")
for n in (5, 10, 20):
    A = (np.diag(4.0 * np.ones(n)) + np.diag(-1.0 * np.ones(n - 1), 1)
         + np.diag(-1.0 * np.ones(n - 1), -1))
    b = np.ones(n)
    for name, run in (("jacobi", jacobi), ("gauss_seidel", gauss_seidel)):
        rho = spectral_radius(iteration_matrix(A, name))
        # Each sweep multiplies the error by rho, so reaching 1e-10 needs
        # log(1e-10) / log(rho) sweeps.
        pred = int(np.ceil(np.log(1e-10) / np.log(rho)))
        _, k, _ = run(A, b, tol=1e-10, max_iter=4000)
        print(f"{n:>6} {name:>14} {rho:>9.5f} {pred:>11} {k:>8}")

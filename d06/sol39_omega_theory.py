"""Problem 6.39: the best omega has a formula, and the formula is worth testing."""
import numpy as np

from nmkit.iterative import iteration_matrix, sor, spectral_radius

print(f"{'size':>6} {'from the formula':>18} {'found by search':>17} {'sweeps':>8}")
for n in (5, 10, 20, 40):
    A = (np.diag(4.0 * np.ones(n)) + np.diag(-1.0 * np.ones(n - 1), 1)
         + np.diag(-1.0 * np.ones(n - 1), -1))
    b = np.ones(n)
    rho_j = spectral_radius(iteration_matrix(A, "jacobi"))
    # For this class of matrix the best omega is 2 / (1 + sqrt(1 - rho**2)).
    w_theory = 2.0 / (1.0 + np.sqrt(1.0 - rho_j ** 2))
    best = min(((sor(A, b, omega=float(w), tol=1e-10, max_iter=4000)[1], float(w))
                for w in np.arange(1.0, 1.99, 0.01)))
    print(f"{n:>6} {w_theory:>18.4f} {best[1]:>17.4f} {best[0]:>8}")

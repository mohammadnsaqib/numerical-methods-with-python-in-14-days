"""Problem 4.36: solve random systems and report the residual rather than trusting the
answer."""
import numpy as np

from nmkit.linsolve import residual, solve

rng = np.random.default_rng(41)
print(f"{'size':>6} {'largest residual':>18} {'gap from numpy':>16}")
for n in (3, 6, 12, 25, 50):
    A = rng.uniform(-4, 4, (n, n))
    x_true = np.arange(1.0, n + 1.0)
    b = A @ x_true
    x = solve(A, b)
    print(f"{n:>6} {np.max(np.abs(residual(A, x, b))):>18.3e} "
          f"{np.max(np.abs(x - np.linalg.solve(A, b))):>16.3e}")

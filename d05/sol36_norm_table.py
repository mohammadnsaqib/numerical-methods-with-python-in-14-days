"""Problem 5.36: one table of every norm of a matrix and of the vectors it acts on."""
import numpy as np

from nmkit.norms import mnorm, vnorm

rng = np.random.default_rng(79)
A = rng.normal(size=(5, 5))
print(f"{'norm':>10} {'of A':>12} {'largest stretch found':>24}")
for name, p in (("1", 1), ("2", 2), ("inf", np.inf)):
    best = max(vnorm(A @ x, p) / vnorm(x, p)
               for x in rng.normal(size=(20000, 5)))
    print(f"{name:>10} {mnorm(A, p):>12.6f} {best:>24.6f}")
print(f"{'fro':>10} {mnorm(A, 'fro'):>12.6f} {'not an induced norm':>24}")

"""A solver is trusted when an independently written one agrees with it on random
problems."""
import numpy as np

from nmkit.linsolve import solve

rng = np.random.default_rng(11)
worst = 0.0
for trial in range(200):
    n = int(rng.integers(2, 9))
    A = rng.uniform(-5, 5, (n, n))
    b = rng.uniform(-5, 5, n)
    if abs(np.linalg.det(A)) < 1e-8:
        continue
    gap = np.max(np.abs(solve(A, b) - np.linalg.solve(A, b)))
    worst = max(worst, gap)
print("200 random systems, sizes 2 to 8")
print("largest disagreement with numpy.linalg.solve:", f"{worst:.3e}")

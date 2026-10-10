"""The determinant is a by-product of the factorisation, not a separate calculation."""
import numpy as np

from nmkit.linsolve import det

rng = np.random.default_rng(31)
print(f"{'size':>6} {'from the factorisation':>24} {'numpy':>24} {'relative gap':>14}")
for n in (2, 3, 5, 8):
    A = rng.uniform(-2, 2, (n, n))
    mine, theirs = det(A), np.linalg.det(A)
    print(f"{n:>6} {mine:>24.14f} {theirs:>24.14f} "
          f"{abs(mine - theirs) / abs(theirs):>14.2e}")

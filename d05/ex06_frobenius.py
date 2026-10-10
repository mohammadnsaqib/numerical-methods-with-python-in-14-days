"""The Frobenius norm is not induced by any vector norm, and it is never smaller than
the 2-norm."""
import numpy as np

from nmkit.norms import mnorm

rng = np.random.default_rng(67)
print(f"{'size':>6} {'2-norm':>12} {'Frobenius':>12} {'ratio':>8} {'sqrt(rank)':>12}")
for n in (2, 4, 8, 16):
    A = rng.normal(size=(n, n))
    two, fro = mnorm(A, 2), mnorm(A, "fro")
    print(f"{n:>6} {two:>12.6f} {fro:>12.6f} {fro / two:>8.4f} {np.sqrt(n):>12.4f}")

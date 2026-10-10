"""Pivoting keeps the entries from growing, and the growth is the quantity that matters.
"""
import numpy as np

from nmkit.linsolve import growth_factor

rng = np.random.default_rng(17)
print(f"{'size':>6} {'growth with pivoting':>22}")
for n in (5, 10, 20, 50, 100):
    worst = max(growth_factor(rng.uniform(-1, 1, (n, n))) for _ in range(20))
    print(f"{n:>6} {worst:>22.3f}")
print("\nfor comparison, the entries of A start at size 1.")

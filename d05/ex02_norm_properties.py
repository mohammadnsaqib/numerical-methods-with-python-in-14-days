"""A norm is not any old size: it obeys three rules, and the third is the one that is
used."""
import numpy as np

from nmkit.norms import vnorm

rng = np.random.default_rng(53)
worst = 0.0
for _ in range(2000):
    x, y = rng.normal(size=5), rng.normal(size=5)
    slack = vnorm(x, 2) + vnorm(y, 2) - vnorm(x + y, 2)
    worst = min(worst, slack)

print("smallest slack in |x + y| <= |x| + |y| over 2000 pairs:", f"{worst:.3e}")
print("scaling: |3x| equals 3|x| ?",
      abs(vnorm(3 * np.ones(4), 2) - 3 * vnorm(np.ones(4), 2)) < 1e-15)
print("only the zero vector has size zero:", vnorm(np.zeros(4), 2) == 0.0)

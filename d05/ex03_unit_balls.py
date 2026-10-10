"""The three norms disagree about which vectors have size one, and by a bounded amount.
"""
import numpy as np

from nmkit.norms import vnorm

rng = np.random.default_rng(59)
n = 8
ratios_12, ratios_2inf = [], []
for _ in range(5000):
    x = rng.normal(size=n)
    ratios_12.append(vnorm(x, 1) / vnorm(x, 2))
    ratios_2inf.append(vnorm(x, 2) / vnorm(x, np.inf))

print(f"n = {n}, so sqrt(n) = {np.sqrt(n):.4f}")
print(f"1-norm / 2-norm   ranges over {min(ratios_12):.4f} to {max(ratios_12):.4f}")
print(f"2-norm / inf-norm ranges over {min(ratios_2inf):.4f} to {max(ratios_2inf):.4f}")
print("both are bounded by 1 and sqrt(n).")

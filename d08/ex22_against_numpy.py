"""Two independent implementations of the same polynomial, checked away from the nodes.
"""
import numpy as np
from scipy.interpolate import BarycentricInterpolator

from nmkit.interp import chebyshev_nodes, divided_differences, newton_eval

# BarycentricInterpolator PERMUTES its points internally to improve conditioning, and it
# draws that permutation from numpy's legacy global generator. Two runs of this program
# with identical inputs therefore differ in the last digits of the gap below -- measured
# at 1.09e-11 and 1.78e-11 on consecutive runs -- and every capture quoting it drifts.
# Seeding the legacy generator fixes the permutation and makes the run reproducible.
np.random.seed(0)
rng = np.random.default_rng(167)
print(f"{'points':>8} {'largest gap from scipy':>24}")
for n in (4, 6, 8, 10, 12):
    xs = chebyshev_nodes(-1.0, 1.0, n)
    ys = rng.uniform(-2, 2, n)
    t = np.linspace(-1, 1, 300)
    mine = newton_eval(xs, divided_differences(xs, ys)[0], t)
    theirs = BarycentricInterpolator(xs, ys)(t)
    print(f"{n:>8} {np.max(np.abs(mine - theirs)):>24.3e}")

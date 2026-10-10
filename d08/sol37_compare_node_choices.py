"""Problem 8.37: three ways of placing nodes, measured on one function."""
import numpy as np

from nmkit.interp import chebyshev_nodes, lagrange_eval, runge

def random_nodes(a, b, n, seed):
    return np.sort(np.random.default_rng(seed).uniform(a, b, n))

t = np.linspace(-1.0, 1.0, 1000)
print(f"{'points':>7} {'equally spaced':>16} {'random':>14} {'Chebyshev':>13}")
for n in (7, 11, 15, 19):
    rows = []
    for xs in (np.linspace(-1, 1, n), random_nodes(-1, 1, n, 100 + n),
               chebyshev_nodes(-1, 1, n)):
        rows.append(np.max(np.abs(runge(t) - lagrange_eval(xs, runge(xs), t))))
    print(f"{n:>7} {rows[0]:>16.3e} {rows[1]:>14.3e} {rows[2]:>13.3e}")

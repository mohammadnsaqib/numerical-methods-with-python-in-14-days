"""The same function, the same count of points, and the error falls instead of growing.
"""
import numpy as np

from nmkit.interp import chebyshev_nodes, lagrange_eval, runge

t = np.linspace(-1.0, 1.0, 1000)
print(f"{'points':>8} {'equally spaced':>18} {'Chebyshev':>16}")
for n in (5, 9, 13, 17, 21, 25):
    ev = np.linspace(-1.0, 1.0, n)
    cb = chebyshev_nodes(-1.0, 1.0, n)
    e1 = np.max(np.abs(runge(t) - lagrange_eval(ev, runge(ev), t)))
    e2 = np.max(np.abs(runge(t) - lagrange_eval(cb, runge(cb), t)))
    print(f"{n:>8} {e1:>18.4e} {e2:>16.4e}")

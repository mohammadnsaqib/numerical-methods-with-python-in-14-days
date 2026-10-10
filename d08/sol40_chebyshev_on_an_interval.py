"""Problem 8.40: the nodes moved off [-1, 1] onto any interval, and checked there."""
import numpy as np

from nmkit.interp import chebyshev_nodes, lagrange_eval

def f(x):
    return np.log(x)

a, b = 1.0, 5.0
t = np.linspace(a, b, 800)
print(f"{'points':>7} {'equally spaced':>16} {'Chebyshev':>13}")
for n in (4, 6, 8, 10, 12):
    ev = np.linspace(a, b, n)
    cb = chebyshev_nodes(a, b, n)
    e1 = np.max(np.abs(f(t) - lagrange_eval(ev, f(ev), t)))
    e2 = np.max(np.abs(f(t) - lagrange_eval(cb, f(cb), t)))
    print(f"{n:>7} {e1:>16.3e} {e2:>13.3e}")
print("\nthe nodes are inside [1, 5] and the smallest "
      "is", f"{chebyshev_nodes(a, b, 8)[0]:.6f}")

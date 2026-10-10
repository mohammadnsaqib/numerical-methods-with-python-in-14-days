"""Problem 11.38: five formulas, one measured order each, on one function."""
import numpy as np

from nmkit.diff import (backward_diff, central_diff, five_point, forward_diff,
                        second_diff)

x = 1.0


def three_point_end(f, xx, h):
    """A one-sided formula that is second order, for use where no left neighbour exists.
    """
    return (-3 * f(xx) + 4 * f(xx + h) - f(xx + 2 * h)) / (2 * h)


cases = [("forward", forward_diff, np.cos(x)),
         ("backward", backward_diff, np.cos(x)),
         ("one-sided, three point", three_point_end, np.cos(x)),
         ("centred", central_diff, np.cos(x)),
         ("five point", five_point, np.cos(x)),
         ("second derivative", second_diff, -np.sin(x))]

print(f"{'formula':>23} {'error at h/2':>14} {'error at h/4':>14} "
      f"{'measured order':>16}")
for name, fn, exact in cases:
    e2 = abs(fn(np.sin, x, 0.02) - exact)
    e4 = abs(fn(np.sin, x, 0.01) - exact)
    print(f"{name:>23} {e2:>14.3e} {e4:>14.3e} {np.log2(e2 / e4):>16.4f}")

"""The simplest piecewise interpolant is straight lines, and it already beats a high
polynomial."""
import numpy as np

from nmkit.interp import runge
from nmkit.spline import piecewise_linear

t = np.linspace(-1.0, 1.0, 1000)
print(f"{'points':>8} {'piecewise linear':>18}")
for n in (5, 9, 17, 33, 65):
    xs = np.linspace(-1.0, 1.0, n)
    e = np.max(np.abs(runge(t) - piecewise_linear(xs, runge(xs), t)))
    print(f"{n:>8} {e:>18.4e}")

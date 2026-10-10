"""One polynomial of high degree against many of low degree, on the function that broke
Day 8."""
import numpy as np

from nmkit.interp import lagrange_eval, runge
from nmkit.spline import cubic_spline, spline_eval

t = np.linspace(-1.0, 1.0, 1000)
print(f"{'points':>8} {'one polynomial':>17} {'a cubic spline':>17}")
for n in (9, 13, 17, 21, 25):
    xs = np.linspace(-1.0, 1.0, n)
    ys = runge(xs)
    e1 = np.max(np.abs(runge(t) - lagrange_eval(xs, ys, t)))
    e2 = np.max(np.abs(runge(t) - spline_eval(xs, ys, cubic_spline(xs, ys), t)))
    print(f"{n:>8} {e1:>17.4e} {e2:>17.4e}")

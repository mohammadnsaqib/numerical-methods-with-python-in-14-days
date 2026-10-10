"""Problem 9.37: four interpolants on one function, measured the same way."""
import numpy as np

from nmkit.interp import lagrange_eval, runge
from nmkit.spline import (cubic_spline, hermite_eval, pchip_slopes, piecewise_linear,
                          spline_eval)

t = np.linspace(-1.0, 1.0, 1200)
print(f"{'knots':>7} {'polynomial':>13} {'linear':>11} {'spline':>11} {'shape':>11}")
for n in (9, 13, 17, 21):
    xs = np.linspace(-1.0, 1.0, n)
    ys = runge(xs)
    row = [np.max(np.abs(runge(t) - lagrange_eval(xs, ys, t))),
           np.max(np.abs(runge(t) - piecewise_linear(xs, ys, t))),
           np.max(np.abs(runge(t) - spline_eval(xs, ys, cubic_spline(xs, ys), t))),
           np.max(np.abs(runge(t) - hermite_eval(xs, ys, pchip_slopes(xs, ys), t)))]
    print(f"{n:>7} {row[0]:>13.3e} {row[1]:>11.3e} {row[2]:>11.3e} {row[3]:>11.3e}")

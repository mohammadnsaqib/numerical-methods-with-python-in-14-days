"""Problem 9.39: a third end condition, and how it compares with the other two."""
import numpy as np
from scipy.interpolate import CubicSpline

from nmkit.spline import cubic_spline, spline_eval

xs = np.linspace(0.0, 3.0, 7)
ys = np.sin(xs)
t = np.linspace(0.0, 3.0, 800)

nat = np.max(np.abs(np.sin(t) - spline_eval(xs, ys, cubic_spline(xs, ys), t)))
cla = np.max(np.abs(np.sin(t) - spline_eval(xs, ys, cubic_spline(
    xs, ys, bc="clamped", slopes=(np.cos(0.0), np.cos(3.0))), t)))
# "Not a knot" asks the third derivative to match across the first and last interior
# knots, which is the same as saying the first two pieces are one cubic. scipy's
# default.
nak = np.max(np.abs(np.sin(t) - CubicSpline(xs, ys, bc_type="not-a-knot")(t)))

print(f"natural   : {nat:.4e}")
print(f"not-a-knot: {nak:.4e}")
print(f"clamped   : {cla:.4e}")
print("\nclamped needs the true slopes; not-a-knot needs nothing and is nearly as "
      "good.")

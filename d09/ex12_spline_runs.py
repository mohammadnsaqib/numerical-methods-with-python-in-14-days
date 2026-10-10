"""The routine reproduces the data and is checked against an independent implementation.
"""
import numpy as np
from scipy.interpolate import CubicSpline

from nmkit.spline import cubic_spline, spline_eval

rng = np.random.default_rng(181)
xs = np.sort(rng.uniform(0, 10, 9))
ys = rng.uniform(-3, 3, 9)
t = np.linspace(xs[0], xs[-1], 500)

m = cubic_spline(xs, ys, bc="natural")
mine = spline_eval(xs, ys, m, t)
theirs = CubicSpline(xs, ys, bc_type="natural")(t)
print("reproduces the data:", np.allclose(spline_eval(xs, ys, m, xs), ys))
print("largest gap from scipy:", f"{np.max(np.abs(mine - theirs)):.3e}")

"""A smooth spline can rise above every value it was given, which for some data is
wrong."""
import numpy as np

from nmkit.spline import cubic_spline, spline_eval

xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
ys = np.array([0.0, 0.0, 0.0, 1.0, 1.0, 1.0])  # a step: never above 1, never below 0
t = np.linspace(0.0, 5.0, 2000)
v = spline_eval(xs, ys, cubic_spline(xs, ys), t)

print("data range     :", ys.min(), "to", ys.max())
print("spline range   :", f"{v.min():.6f}", "to", f"{v.max():.6f}")
print("overshoot above:", f"{v.max() - ys.max():.6f}")
print("undershoot below:", f"{ys.min() - v.min():.6f}")

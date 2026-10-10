"""Choosing the slopes instead of the curvatures removes the overshoot entirely."""
import numpy as np

from nmkit.spline import cubic_spline, hermite_eval, pchip_slopes, spline_eval

xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
ys = np.array([0.0, 0.0, 0.0, 1.0, 1.0, 1.0])
t = np.linspace(0.0, 5.0, 2000)

spl = spline_eval(xs, ys, cubic_spline(xs, ys), t)
her = hermite_eval(xs, ys, pchip_slopes(xs, ys), t)
print("cubic spline range :", f"{spl.min():.6f}", "to", f"{spl.max():.6f}")
print("shape-preserving   :", f"{her.min():.6f}", "to", f"{her.max():.6f}")
print("the second never leaves the range of the data:",
      bool(her.min() >= ys.min() - 1e-12 and her.max() <= ys.max() + 1e-12))

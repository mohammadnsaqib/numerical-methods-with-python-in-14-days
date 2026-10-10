"""A spline through ten thousand points, evaluated a hundred thousand times."""
import numpy as np

from nmkit.spline import cubic_spline, spline_eval

n = 10000
xs = np.linspace(0.0, 100.0, n)
ys = np.sin(xs) * np.exp(-xs / 50.0)
m = cubic_spline(xs, ys)

t = np.linspace(0.0, 100.0, 100000)
vals = spline_eval(xs, ys, m, t)
true = np.sin(t) * np.exp(-t / 50.0)
print("knots      :", n)
print("evaluations:", t.size)
print("largest error:", f"{np.max(np.abs(vals - true)):.3e}")

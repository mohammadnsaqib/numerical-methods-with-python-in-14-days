"""Problem 9.41: a curve in the plane, splined against its own arc length."""
import numpy as np

from nmkit.spline import cubic_spline, spline_eval

# A spiral. Splining y against x would fail, because x is not increasing along it.
th = np.linspace(0.0, 4.0 * np.pi, 15)
px, py = th * np.cos(th), th * np.sin(th)

# The parameter is the running distance along the polygon through the points.
seg = np.hypot(np.diff(px), np.diff(py))
s = np.concatenate([[0.0], np.cumsum(seg)])

mx, my = cubic_spline(s, px), cubic_spline(s, py)
fine = np.linspace(s[0], s[-1], 1500)
qx, qy = spline_eval(s, px, mx, fine), spline_eval(s, py, my, fine)

print("points          :", th.size)
print("x is increasing :", bool(np.all(np.diff(px) > 0)))
print("s is increasing :", bool(np.all(np.diff(s) > 0)))
print("passes through every point:",
      bool(max(np.max(np.abs(spline_eval(s, px, mx, s) - px)),
               np.max(np.abs(spline_eval(s, py, my, s) - py))) < 1e-10))
print("length of the polygon :", f"{s[-1]:.6f}")
print("length of the spline  :",
      f"{np.sum(np.hypot(np.diff(qx), np.diff(qy))):.6f}")

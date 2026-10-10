"""Halving the spacing divides the error by sixteen: a cubic spline is fourth order."""
import numpy as np

from nmkit.spline import cubic_spline, spline_eval

f = np.sin
t = np.linspace(0.0, 3.0, 3000)
print(f"{'pieces':>8} {'error':>13} {'ratio':>9}")
prev = None
for n in (5, 9, 17, 33, 65):
    xs = np.linspace(0.0, 3.0, n)
    ys = f(xs)
    e = np.max(np.abs(f(t) - spline_eval(xs, ys, cubic_spline(xs, ys, bc="clamped",
                                                              slopes=(np.cos(0.0),
                                                                      np.cos(3.0))),
                                                                      t)))
    ratio = f"{e / prev:.5f}" if prev else "     --"
    print(f"{n - 1:>8} {e:>13.4e} {ratio:>9}")
    prev = e

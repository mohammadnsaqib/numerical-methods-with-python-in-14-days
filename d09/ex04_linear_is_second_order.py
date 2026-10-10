"""Halving the spacing quarters the error: piecewise linear is second order in the
spacing."""
import numpy as np

from nmkit.spline import piecewise_linear

f = np.sin
t = np.linspace(0.0, 3.0, 2000)
print(f"{'pieces':>8} {'spacing':>10} {'error':>13} {'ratio':>9}")
prev = None
for n in (5, 9, 17, 33, 65):
    xs = np.linspace(0.0, 3.0, n)
    e = np.max(np.abs(f(t) - piecewise_linear(xs, f(xs), t)))
    ratio = f"{e / prev:.5f}" if prev else "     --"
    print(f"{n - 1:>8} {3.0 / (n - 1):>10.5f} {e:>13.4e} {ratio:>9}")
    prev = e

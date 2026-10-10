"""The end condition changes the answer near the ends and almost nothing in the middle.
"""
import numpy as np

from nmkit.spline import cubic_spline, spline_eval

xs = np.linspace(0.0, 3.0, 7)
ys = np.sin(xs)
nat = cubic_spline(xs, ys, bc="natural")
cla = cubic_spline(xs, ys, bc="clamped", slopes=(np.cos(0.0), np.cos(3.0)))

print(f"{'x':>7} {'natural':>13} {'clamped':>13} {'true':>13}")
for x in (0.05, 0.4, 1.5, 2.6, 2.95):
    print(f"{x:>7.2f} {spline_eval(xs, ys, nat, x):>13.8f} "
          f"{spline_eval(xs, ys, cla, x):>13.8f} {np.sin(x):>13.8f}")

"""Problem 9.40: how far a spline overshoots as the step in the data gets sharper."""
import numpy as np

from nmkit.spline import cubic_spline, hermite_eval, pchip_slopes, spline_eval

xs = np.arange(0.0, 6.0)
t = np.linspace(0.0, 5.0, 2000)
print(f"{'step size':>11} {'spline max':>13} {'overshoot':>12} {'shape max':>12}")
for h in (0.25, 0.5, 1.0, 2.0, 4.0):
    ys = np.array([0.0, 0.0, 0.0, h, h, h])
    s = spline_eval(xs, ys, cubic_spline(xs, ys), t)
    p = hermite_eval(xs, ys, pchip_slopes(xs, ys), t)
    print(f"{h:>11.2f} {s.max():>13.6f} {s.max() - h:>12.6f} {p.max():>12.6f}")
print("\nthe overshoot is a fixed FRACTION of the step, not a fixed amount.")

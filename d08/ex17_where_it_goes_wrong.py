"""The failure is at the ENDS, and the middle is fine throughout."""
import numpy as np

from nmkit.interp import lagrange_eval, runge

xs = np.linspace(-1.0, 1.0, 17)
p = lambda t: lagrange_eval(xs, runge(xs), t)

print(f"{'x':>8} {'true':>12} {'interpolant':>16} {'error':>14}")
for x in (0.0, 0.3, 0.6, 0.85, 0.95, 0.99):
    print(f"{x:>8.2f} {runge(x):>12.6f} {p(x):>16.6f} {abs(p(x) - runge(x)):>14.4e}")

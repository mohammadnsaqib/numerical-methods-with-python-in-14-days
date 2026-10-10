"""Problem 8.41: asking for a value outside the nodes, and what it costs."""
import numpy as np

from nmkit.interp import lagrange_eval

xs = np.linspace(0.0, 1.0, 7)
f = np.exp
print(f"{'x':>7} {'inside?':>9} {'interpolant':>15} {'true':>13} {'error':>12}")
errs = {}
for x in (0.5, 0.95, 1.0, 1.1, 1.3, 1.6):
    p = lagrange_eval(xs, f(xs), x)
    inside = "yes" if 0.0 <= x <= 1.0 else "NO"
    errs[x] = abs(p - f(x))
    print(f"{x:>7.2f} {inside:>9} {p:>15.8f} {f(x):>13.8f} {errs[x]:>12.2e}")
# Computed, not asserted. An earlier draft claimed "thirty thousand times" from memory.
print(f"\nthe error at 1.6 is {errs[1.6] / errs[0.95]:.0f} times the error at 0.95.")

"""A damped spring, whose three regimes are one parameter apart."""
import numpy as np

from nmkit.ode import rk4, to_system

K = 4.0
print(f"{'damping':>9} {'regime':>16} {'y(4)':>13} {'sign changes':>14}")
for c in (0.5, 4.0, 8.0):
    f = to_system(lambda t, y, c=c: -c * y[1] - K * y[0], 2)
    ts, ys = rk4(f, 0.0, [1.0, 0.0], 0.001, 4000)
    regime = ("under" if c * c < 4 * K else ("critical" if c * c == 4 * K else "over"))
    crossings = int(np.sum(np.diff(np.sign(ys[:, 0])) != 0))
    print(f"{c:>9.1f} {regime + ' damped':>16} {ys[-1, 0]:>13.9f} {crossings:>14}")
print()
print(f"the boundary is at c squared = 4k, which is c = {np.sqrt(4 * K):.1f}")
print("below it the spring oscillates through zero. At and above it, it never does.")

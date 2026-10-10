"""Problem 13.36: a cooling body, solved numerically and checked against its own law."""
import numpy as np

from nmkit.ode import rk4

AMBIENT, K = 20.0, 0.18


def f(t, y):
    """Newton's law of cooling: the rate is proportional to the excess over the room."""
    return -K * (y - AMBIENT)


def exact(t):
    """The closed-form solution from an initial temperature of 95 degrees."""
    return AMBIENT + (95.0 - AMBIENT) * np.exp(-K * t)


ts, ys = rk4(f, 0.0, 95.0, 0.05, 600)
print(f"{'minutes':>9} {'computed':>12} {'exact':>12} {'error':>12}")
for k in (0, 100, 200, 400, 600):
    print(f"{ts[k]:>9.1f} {ys[k]:>12.6f} {exact(ts[k]):>12.6f} "
          f"{abs(ys[k] - exact(ts[k])):>12.3e}")
print()
half = ts[int(np.argmin(np.abs(ys - (AMBIENT + (95.0 - AMBIENT) / 2))))]
print(f"the grid, spaced {ts[1] - ts[0]:.2f} minutes apart, puts the halving at "
      f"{half:.2f}")
print(f"the law says ln(2)/k = {np.log(2) / K:.6f} minutes")
print(f"they differ by {abs(half - np.log(2) / K):.4f}, which is less than one grid "
      f"spacing")

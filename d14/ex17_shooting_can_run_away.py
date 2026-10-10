"""A nonlinear problem where a guess a little too large never comes back."""
import numpy as np

from nmkit.ode import rk4


def f(t, y):
    """y'' = y^3 - y, which grows without bound once y climbs past 1."""
    return np.array([y[1], y[0] ** 3 - y[0]])


last_ok, first_bad = None, None
print(f"{'slope tried':>12} {'value at t = 3':>18} {'what happened':>18}")
for s in (0.1, 0.3, 0.5, 0.6, 0.7, 0.8):
    with np.errstate(over="ignore", invalid="ignore"):
        _, ys = rk4(f, 0.0, [0.5, s], 3.0 / 600, 600)
    v = float(ys[-1, 0])
    ok = np.isfinite(v) and abs(v) < 1e6
    if ok:
        last_ok = s
    elif first_bad is None:
        first_bad = s
    print(f"{s:>12.2f} {v:>18.6e} {'finite' if ok else 'overflowed':>18}")
print()
print(f"between {last_ok} and {first_bad} the trajectory stops coming back. A root")
print("finder handed this function gets nothing usable for an answer.")
print("Nothing is wrong with the boundary problem. The METHOD chose to march.")

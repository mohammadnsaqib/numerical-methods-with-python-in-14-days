"""Four methods, judged on evaluations rather than on steps."""
import numpy as np

from nmkit.ode import euler, heun, midpoint_ode, rk4


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


methods = [("Euler", euler, 1), ("Heun", heun, 2), ("midpoint", midpoint_ode, 2),
           ("RK4", rk4, 4)]
print(f"{'calls':>7} " + " ".join(f"{name:>12}" for name, _, _ in methods))
for calls in (80, 160, 320, 640, 1280):
    row = []
    for name, m, cost in methods:
        n = calls // cost
        row.append(abs(float(m(f, 0.0, 0.5, 2.0 / n, n)[1][-1]) - exact(2.0)))
    print(f"{calls:>7} " + " ".join(f"{v:>12.3e}" for v in row))
print()
print("RK4 spends four evaluations per step and is still ahead of Euler by",
      f"{np.log10(row[0] / row[3]):.1f} decades at 1280")

"""Six slopes, two answers, and a difference that estimates the error for free."""
import numpy as np

from nmkit.ode import rk45_step


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


t0 = 1.0
start = np.array([exact(t0)])
print(f"{'h':>8} {'the difference':>16} {'error of y4':>14} {'ratio':>7} "
      f"{'error of y5':>14}")
for h in (0.4, 0.2, 0.1, 0.05, 0.025):
    y4, y5, diff = rk45_step(f, t0, start, h)
    e4 = abs(float(y4[0]) - exact(t0 + h))
    e5 = abs(float(y5[0]) - exact(t0 + h))
    print(f"{h:>8.4f} {diff:>16.3e} {e4:>14.3e} {diff / e4:>7.3f} {e5:>14.3e}")
print()
print("the difference tracks the FOURTH-order answer's error to three digits. The step")
print("is then taken with the fifth-order answer, "
      "which is better than the estimate says.")

"""Guess the missing slope, integrate, and see where it lands."""
import numpy as np

from nmkit.ode import rk4


def f(t, y):
    """y'' = -y, wanted with y(0) = 0 and y(pi/2) = 1."""
    return np.array([y[1], -y[0]])


B = np.pi / 2
print(f"{'slope tried':>12} {'value at pi/2':>16} {'miss':>14}")
for s in (0.0, 0.5, 1.0, 1.5, 2.0):
    _, ys = rk4(f, 0.0, [0.0, s], B / 200, 200)
    print(f"{s:>12.4f} {ys[-1, 0]:>16.10f} {ys[-1, 0] - 1.0:>14.10f}")
print()
print("the miss is a straight line in the slope, because the equation is linear.")
print("finding where it crosses zero is a "
      "root-finding problem, and Day 2 solved those.")

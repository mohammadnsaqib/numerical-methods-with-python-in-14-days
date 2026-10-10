"""Problem 14.36: two bodies in orbit, checked by two quantities the motion holds fixed.
"""
import numpy as np

from nmkit.ode import rk4


def f(t, y):
    """Position y[0], y[1] and velocity y[2], y[3], under an inverse-square attraction.
    """
    r = np.hypot(y[0], y[1])
    return np.array([y[2], y[3], -y[0] / r ** 3, -y[1] / r ** 3])


# A circular orbit of radius 1 needs a speed of 1. Starting off that speed gives an
# ellipse.
start = [1.0, 0.0, 0.0, 1.1]
ts, ys = rk4(f, 0.0, start, 0.0005, 40000)
r = np.hypot(ys[:, 0], ys[:, 1])
speed2 = ys[:, 2] ** 2 + ys[:, 3] ** 2
energy = 0.5 * speed2 - 1.0 / r
angular = ys[:, 0] * ys[:, 3] - ys[:, 1] * ys[:, 2]

print(f"steps            : {ts.size - 1}")
print(f"time covered     : {ts[-1]:.1f}, about {ts[-1] / (2 * np.pi):.2f} orbits")
print(f"closest approach : {r.min():.9f}")
print(f"furthest         : {r.max():.9f}")
print()
print(f"{'quantity':>18} {'at the start':>16} {'at the end':>16} {'drift':>12}")
for name, q in (("energy", energy), ("angular momentum", angular)):
    print(f"{name:>18} {q[0]:>16.12f} {q[-1]:>16.12f} {abs(q[-1] - q[0]):>12.3e}")
print()
print("neither quantity was used to compute the orbit, and neither needs a formula")
print("for it. They are the check Day 13 called "
      "for on a problem that has no closed form.")

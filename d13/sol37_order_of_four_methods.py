"""Problem 13.37: four methods, one measured order each, on one equation."""
import numpy as np

from nmkit.ode import euler, heun, midpoint_ode, rk4


def f(t, y):
    return np.cos(t) - y


def exact(t):
    return (np.sin(t) + np.cos(t) - np.exp(-t)) / 2


methods = [("Euler", euler, 1), ("Heun", heun, 2), ("midpoint", midpoint_ode, 2),
           ("RK4", rk4, 4)]
print(f"{'method':>10} {'claimed':>9} {'n = 100':>12} {'n = 200':>12} {'n = 400':>12} "
      f"{'measured':>10}")
for name, m, claimed in methods:
    e = [abs(float(m(f, 0.0, 0.0, 4.0 / n, n)[1][-1]) - exact(4.0))
         for n in (100, 200, 400)]
    print(f"{name:>10} {claimed:>9} {e[0]:>12.3e} {e[1]:>12.3e} {e[2]:>12.3e} "
          f"{np.log2(e[1] / e[2]):>10.4f}")

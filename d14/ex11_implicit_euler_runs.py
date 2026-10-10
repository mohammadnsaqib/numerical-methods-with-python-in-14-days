"""No step is too long for stability, and the step is now chosen for accuracy alone."""
import numpy as np

from nmkit.ode import euler, euler_implicit


def f(t, y):
    return -1000.0 * y + 999.0 * np.exp(-t)


def exact(t):
    return np.exp(-1000 * t) + np.exp(-t)


print(f"{'h':>8} {'steps':>7} {'explicit y(3)':>18} {'implicit y(3)':>16} "
      f"{'implicit error':>16}")
for h in (0.5, 0.2, 0.1, 0.01, 0.002):
    n = int(round(3.0 / h))
    _, e = euler(f, 0.0, 2.0, h, n)
    _, i = euler_implicit(f, 0.0, 2.0, h, n)
    print(f"{h:>8.3f} {n:>7} {float(e[-1]):>18.4e} {float(i[-1]):>16.9f} "
          f"{abs(float(i[-1]) - exact(3.0)):>16.3e}")
print()
print(f"the exact value is {exact(3.0):.9f}")
print("at h = 0.5 the implicit method takes six steps and is right to three digits.")

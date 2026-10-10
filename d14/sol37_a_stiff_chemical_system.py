"""Problem 14.37: a stiff system where the explicit method is not merely slower."""
import numpy as np

from nmkit.ode import euler, euler_implicit


def f(t, y):
    """Three species: y[0] decays slowly, y[1] is short-lived, y[2] accumulates."""
    a = 0.04 * y[0]
    b = 1e4 * y[1] * y[2]
    c = 3e7 * y[1] ** 2
    return np.array([-a + b, a - b - c, c])


T = 0.4
print(f"{'method':>16} {'steps':>8} {'y0':>13} {'y1':>13} {'y2':>13} {'sum':>13}")
for name, m, n in (("explicit Euler", euler, 200),
                   ("explicit Euler", euler, 20000),
                   ("implicit Euler", euler_implicit, 200)):
    with np.errstate(over="ignore", invalid="ignore"):
        _, ys = m(f, 0.0, [1.0, 0.0, 0.0], T / n, n)
    v = ys[-1]
    print(f"{name:>16} {n:>8} {v[0]:>13.6e} {v[1]:>13.6e} {v[2]:>13.6e} "
          f"{float(np.sum(v)):>13.9f}")
print()
print("the three amounts must add to 1 for ever, because nothing leaves the system.")
print("the implicit method holds that at 200 steps. The explicit one does not hold it")
print("at 200 and needs twenty thousand to get there.")

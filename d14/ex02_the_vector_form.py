"""The same routine on systems of two, three and four equations, unchanged."""
import numpy as np

from nmkit.ode import rk4


def chain(k):
    """k tanks in a row, each draining into the next at a rate set by its own level."""
    def f(t, y):
        out = np.zeros(k)
        out[0] = -y[0]
        for i in range(1, k):
            out[i] = y[i - 1] - y[i]
        return out
    return f


print(f"{'equations':>11} {'sum at t = 0':>14} {'sum at t = 3':>14} {'first tank':>12}")
for k in (2, 3, 4):
    y0 = np.zeros(k)
    y0[0] = 1.0
    ts, ys = rk4(chain(k), 0.0, y0, 0.001, 3000)
    print(f"{k:>11} {float(np.sum(ys[0])):>14.9f} {float(np.sum(ys[-1])):>14.9f} "
          f"{ys[-1, 0]:>12.9f}")
print()
print(f"the first tank always holds exp(-3) = {float(np.exp(-3.0)):.9f}, whatever "
      f"follows it")
print("not one line of the solver knows how many equations it was given")

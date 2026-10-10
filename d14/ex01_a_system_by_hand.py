"""Two quantities whose rates depend on each other, stepped together."""
import numpy as np

from nmkit.ode import rk4


def f(t, y):
    """A circuit: y[0] is a charge and y[1] a current, each driving the other."""
    return np.array([y[1], -4.0 * y[0] - 0.5 * y[1]])


ts, ys = rk4(f, 0.0, [1.0, 0.0], 0.01, 600)
print(f"{'t':>5} {'charge':>12} {'current':>12}")
for k in (0, 100, 200, 300, 450, 600):
    print(f"{ts[k]:>5.1f} {ys[k, 0]:>12.6f} {ys[k, 1]:>12.6f}")
print()
print("the two columns are one solution, not two. Neither can be computed alone.")

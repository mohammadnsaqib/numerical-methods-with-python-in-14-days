"""Problem 13.38: a system of two equations, solved by a routine that was never told."""
import numpy as np

from nmkit.ode import rk4


def f(t, y):
    """A predator and its prey: y[0] grows and is eaten, y[1] eats and dies."""
    return np.array([0.8 * y[0] - 0.4 * y[0] * y[1],
                     -0.5 * y[1] + 0.2 * y[0] * y[1]])


ts, ys = rk4(f, 0.0, [2.0, 1.0], 0.01, 4000)
print(f"{'t':>6} {'prey':>12} {'predator':>12}")
for k in (0, 500, 1000, 2000, 3000, 4000):
    print(f"{ts[k]:>6.1f} {ys[k, 0]:>12.6f} {ys[k, 1]:>12.6f}")
print()

# This system has a quantity that does not change along a solution. Anything the method
# does to that quantity is error, and it needs no closed-form solution to see it.
def invariant(y):
    """0.2 y0 - 0.5 ln(y0) + 0.4 y1 - 0.8 ln(y1), constant along every solution."""
    return 0.2 * y[:, 0] - 0.5 * np.log(y[:, 0]) + 0.4 * y[:, 1] - 0.8 * np.log(y[:, 1])


v = invariant(ys)
print(f"the conserved quantity starts at {v[0]:.12f}")
print(f"after 4000 steps it is          {v[-1]:.12f}")
print(f"it drifted by                   {abs(v[-1] - v[0]):.3e}")

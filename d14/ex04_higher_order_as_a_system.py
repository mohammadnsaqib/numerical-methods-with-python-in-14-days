"""A second-order equation, rewritten as two first-order ones and solved unchanged."""
import numpy as np

from nmkit.ode import rk4, to_system

# y'' = -4y, y(0) = 1, y'(0) = 0. Naming y[0] = y and y[1] = y' makes the first row read
# y[0]' = y[1], which is true by definition, and only the second row carries the
# equation.
f = to_system(lambda t, y: -4.0 * y[0], 2)
ts, ys = rk4(f, 0.0, [1.0, 0.0], 0.001, 2000)

print(f"{'t':>5} {'computed y':>14} {'cos(2t)':>14} {'computed y prime':>18} "
      f"{'-2 sin(2t)':>13}")
for k in (0, 500, 1000, 1500, 2000):
    t = ts[k]
    print(f"{t:>5.1f} {ys[k, 0]:>14.9f} {np.cos(2 * t):>14.9f} {ys[k, 1]:>18.9f} "
          f"{-2 * np.sin(2 * t):>13.9f}")
print()
print(f"largest error in the value: {np.max(np.abs(ys[:, 0] - np.cos(2 * ts))):.3e}")

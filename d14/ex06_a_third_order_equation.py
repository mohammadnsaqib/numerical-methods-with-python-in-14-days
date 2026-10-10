"""An equation of order three, and the same routine again."""
import numpy as np

from nmkit.ode import rk4, to_system

# y''' - 2y'' - y' + 2y = 0 has solutions exp(t), exp(-t) and exp(2t). With y(0) = 3,
# y'(0) = 2 and y''(0) = 6 the combination is exactly exp(t) + exp(-t) + exp(2t).
f = to_system(lambda t, y: 2 * y[2] + y[1] - 2 * y[0], 3)
ts, ys = rk4(f, 0.0, [3.0, 2.0, 6.0], 0.0005, 4000)


def exact(t):
    return np.exp(t) + np.exp(-t) + np.exp(2 * t)


print(f"{'t':>5} {'computed':>16} {'exact':>16} {'error':>12}")
for k in (0, 1000, 2000, 3000, 4000):
    print(f"{ts[k]:>5.2f} {ys[k, 0]:>16.9f} {exact(ts[k]):>16.9f} "
          f"{abs(ys[k, 0] - exact(ts[k])):>12.3e}")
print()
print("an equation of order n becomes n equations of order one, and the solver is")
print("the same solver. Only the length of the vector changed.")

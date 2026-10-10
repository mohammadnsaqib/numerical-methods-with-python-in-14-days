"""The library routine, and how few guesses a linear problem needs."""
import numpy as np

from nmkit.bvp import shoot


def f(t, y):
    return np.array([y[1], -y[0]])


ts, ys, s, miss, iters = shoot(f, 0.0, np.pi / 2, 0.0, 1.0, 0.0, 2.0)
print(f"the slope found      : {s:.15f}")
print(f"the true slope is 1  : error {abs(s - 1.0):.3e}")
print(f"the miss at that slope: {miss:.3e}")
print(f"secant steps needed  : {iters}")
print(f"largest error in y   : {np.max(np.abs(ys[:, 0] - np.sin(ts))):.3e}")
print()
print(f"{'t':>6} {'computed':>14} {'sin(t)':>14}")
for k in (0, 50, 100, 150, 200):
    print(f"{ts[k]:>6.4f} {ys[k, 0]:>14.10f} {np.sin(ts[k]):>14.10f}")
print()
print("two secant steps are enough. A straight line is determined by two points, and")
print("the miss is a straight line whenever the equation is.")

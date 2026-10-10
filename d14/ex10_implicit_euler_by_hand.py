"""One implicit step, where the unknown appears on both sides of the equation."""
import numpy as np


def f(t, y):
    """y' = -1000 y + 999 exp(-t)."""
    return -1000.0 * y + 999.0 * np.exp(-t)


t, y, h = 0.0, 2.0, 0.1
t_next = t + h
# The step asks for the value w with w = y + h f(t_next, w). For this equation f is
# linear in y, so the equation can be rearranged: w (1 + 1000 h) = y + 999 h
# exp(-t_next).
print(f"the step to solve : w = {y} + {h} * f({t_next}, w)")
print(f"f is linear here  : w * (1 + 1000 * {h}) = {y} + 999 * {h} * exp(-{t_next})")
w = (y + 999 * h * np.exp(-t_next)) / (1 + 1000 * h)
print(f"so w              = {w:.12f}")
print()
print(f"an EXPLICIT step would give {y + h * f(t, y):.6e}")
print(f"the exact value at t = 0.1 is {np.exp(-100) + np.exp(-0.1):.12f}")
print()
print("the explicit step is off by a factor of ninety. The implicit one is not, and")
print("the difference is which side of the interval the slope was read from.")

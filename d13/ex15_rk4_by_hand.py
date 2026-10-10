"""One classical Runge-Kutta step, with all four slopes shown."""
import numpy as np


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


t, y, h = 0.0, 0.5, 0.2
k1 = f(t, y)
k2 = f(t + h / 2, y + h / 2 * k1)
k3 = f(t + h / 2, y + h / 2 * k2)
k4 = f(t + h, y + h * k3)
print(f"k1, at the start     = {k1:.12f}")
print(f"k2, at the middle    = {k2:.12f}   using k1 to get there")
print(f"k3, at the middle    = {k3:.12f}   using k2 to get there")
print(f"k4, at the end       = {k4:.12f}   using k3 to get there")
print(f"weighted 1, 2, 2, 1  = {(k1 + 2 * k2 + 2 * k3 + k4) / 6:.12f}")
print(f"y + h times that     = {y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6:.12f}")
print(f"the exact value      = {exact(0.2):.12f}")
print()
print(f"RK4's error   : "
      f"{abs(y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6 - exact(0.2)):.12f}")
print(f"Heun's error  : "
      f"{abs(y + h * (k1 + f(t + h, y + h * k1)) / 2 - exact(0.2)):.12f}")
print("the weights 1, 2, 2, 1 over 6 are Simpson's "
      "weights 1, 4, 1 over 6, split in two")

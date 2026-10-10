"""One Heun step, with the trial step shown and then discarded."""
import numpy as np


def f(t, y):
    return y - t ** 2 + 1.0


def exact(t):
    return t ** 2 + 2 * t + 1 - 0.5 * np.exp(t)


t, y, h = 0.0, 0.5, 0.2
k1 = f(t, y)
trial = y + h * k1
k2 = f(t + h, trial)
print(f"slope at the start        k1 = {k1:.10f}")
print(f"a trial step of h times k1     = {trial:.10f}")
print(f"slope THERE               k2 = {k2:.10f}")
print(f"their average                  = {(k1 + k2) / 2:.10f}")
print(f"y + h times the average        = {y + h * (k1 + k2) / 2:.10f}")
print(f"the exact value at t = 0.2     = {exact(0.2):.10f}")
print()
print(f"Heun's error : {abs(y + h * (k1 + k2) / 2 - exact(0.2)):.10f}")
print(f"Euler's error: {abs(y + h * k1 - exact(0.2)):.10f}")
print("the trial step is thrown away. Only the slope it revealed is kept.")

"""A difference of differences loses twice as much, so its best step is much larger."""
import numpy as np

from nmkit.diff import central_diff, second_diff

eps = np.finfo(float).eps
x = 1.0
hs = 10.0 ** np.arange(-1.0, -10.01, -0.1)

first = np.array([abs(central_diff(np.sin, x, h) - np.cos(x)) for h in hs])
second = np.array([abs(second_diff(np.sin, x, h) + np.sin(x)) for h in hs])

print(f"first derivative : round-off grows like eps / h,     "
      f"best h ~ eps^(1/3) = {eps ** (1 / 3):.3e}")
print(f"second derivative: round-off grows like eps / h^2,   "
      f"best h ~ eps^(1/4) = {eps ** (1 / 4):.3e}")
print()
print(f"measured best step, first derivative : {hs[int(np.argmin(first))]:.3e}, "
      f"error {first.min():.3e}")
print(f"measured best step, second derivative: {hs[int(np.argmin(second))]:.3e}, "
      f"error {second.min():.3e}")

"""An error in the direction gives an error in the value that is its SQUARE."""
import numpy as np

from nmkit.eigen import rayleigh

A = np.array([[3.0, 1.0], [1.0, 3.0]])
v = np.array([1.0, 1.0]) / np.sqrt(2)
perp = np.array([1.0, -1.0]) / np.sqrt(2)

print(f"{'tilt':>10} {'Rayleigh quotient':>21} {'error':>12} {'error/tilt**2':>15}")
for e in (1e-1, 1e-2, 1e-3, 1e-4):
    w = v + e * perp
    q = rayleigh(A, w)
    print(f"{e:>10.0e} {q:>21.15f} {abs(q - 4.0):>12.3e} "
          f"{abs(q - 4.0) / e ** 2:>15.6f}")

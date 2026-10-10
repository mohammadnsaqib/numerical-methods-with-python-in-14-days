"""Reading one entry of A x over the matching entry of x is the alternative, and it is
worse."""
import numpy as np

from nmkit.eigen import rayleigh

A = np.array([[3.0, 1.0], [1.0, 3.0]])
v = np.array([1.0, 1.0]) / np.sqrt(2)
perp = np.array([1.0, -1.0]) / np.sqrt(2)

print(f"{'tilt':>8} {'Rayleigh error':>17} {'entry ratio error':>20}")
for e in (1e-1, 1e-2, 1e-3):
    w = v + e * perp
    ratio = (A @ w)[0] / w[0]
    print(f"{e:>8.0e} {abs(rayleigh(A, w) - 4.0):>17.3e} {abs(ratio - 4.0):>20.3e}")

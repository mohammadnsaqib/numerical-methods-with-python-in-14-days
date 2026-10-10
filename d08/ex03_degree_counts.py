"""The degree is fixed by the count of points, and adding one raises it by one."""
import numpy as np

from nmkit.interp import vandermonde_fit

f = np.sin
for n in (2, 3, 4, 5, 6):
    xs = np.linspace(0.0, 3.0, n)
    c = vandermonde_fit(xs, f(xs))
    top = np.max(np.abs(c[-1]))
    print(f"{n} points -> degree {n - 1}, leading coefficient {c[-1]:+.8f}")

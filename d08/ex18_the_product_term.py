"""The product over the nodes is enormous near the ends and tiny in the middle."""
import numpy as np

from nmkit.interp import error_product

for n in (9, 17):
    xs = np.linspace(-1.0, 1.0, n)
    t = np.linspace(-1.0, 1.0, 2001)
    prod = np.abs(error_product(xs, t))
    mid = np.max(prod[np.abs(t) < 0.5])
    end = np.max(prod[np.abs(t) > 0.8])
    print(f"{n} equally spaced points: middle {mid:.4e}, near the ends {end:.4e}, "
          f"ratio {end / mid:.1f}")

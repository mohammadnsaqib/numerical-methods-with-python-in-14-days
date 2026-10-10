"""Problem 8.39: the error bound, tested rather than quoted, on three functions."""
import math

import numpy as np

from nmkit.interp import error_product, lagrange_eval

t = np.linspace(0.0, 1.0, 500)
n = 6
xs = np.linspace(0.0, 1.0, n)
fact = float(math.factorial(n))

cases = [
    ("exp(x)   ", np.exp, np.e),                      # the 6th derivative of exp is exp
    ("sin(x)   ", np.sin, 1.0),  # every derivative of sin is at most 1
    # the 6th derivative is 720/(1+x)**7
    ("1/(1+x)  ", lambda v: 1.0 / (1.0 + v), 720.0),
]
for name, f, dmax in cases:
    actual = np.max(np.abs(f(t) - lagrange_eval(xs, f(xs), t)))
    bound = np.max(np.abs(error_product(xs, t))) * dmax / fact
    print(f"{name}: actual {actual:.4e}   bound {bound:.4e}   holds: {actual <= bound}")

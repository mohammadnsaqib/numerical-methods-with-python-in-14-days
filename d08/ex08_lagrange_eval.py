"""The sum of y times basis passes through every point by construction, with nothing
solved."""
import numpy as np

from nmkit.interp import lagrange_eval

xs = np.array([0.0, 1.0, 2.0, 4.0])
ys = np.array([1.0, 3.0, 2.0, 5.0])

print("at the nodes:", np.array2string(lagrange_eval(xs, ys, xs), precision=12))
print("wanted      :", ys)
print("at x = 3    :", f"{lagrange_eval(xs, ys, 3.0):.12f}")
print("no system was solved, so nothing could be ill-conditioned.")

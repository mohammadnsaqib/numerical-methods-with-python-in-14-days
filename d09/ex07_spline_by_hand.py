"""The second derivatives at the knots are the unknowns, and everything else follows."""
import numpy as np

from nmkit.spline import cubic_spline, spline_eval

xs = np.array([0.0, 1.0, 2.0, 3.0])
ys = np.array([0.0, 1.0, 0.0, 2.0])
m = cubic_spline(xs, ys, bc="natural")

print("second derivatives at the knots:", np.array2string(m, precision=10))
print("the two ends are zero, which is what 'natural' means")
print("values back at the knots       :",
      np.array2string(spline_eval(xs, ys, m, xs), precision=12))
print("the data                       :", ys)

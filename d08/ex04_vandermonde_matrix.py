"""The definition written as a linear system: one equation per point."""
import numpy as np

from nmkit.interp import vandermonde_fit, vandermonde_matrix

xs = np.array([0.0, 1.0, 2.0])
ys = np.array([1.0, 3.0, 2.0])
V = vandermonde_matrix(xs)
print("the matrix:\n", V)
c = vandermonde_fit(xs, ys)
print("coefficients:", np.array2string(c, precision=10))
print("V @ c        :", np.array2string(V @ c, precision=10))
print("the values wanted:", ys)

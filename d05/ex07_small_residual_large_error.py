"""A residual near the format's floor is compatible with an answer that is entirely
wrong."""
import numpy as np

from nmkit.linsolve import residual, solve
from nmkit.norms import hilbert, vnorm

n = 12
A = hilbert(n)
x_true = np.ones(n)
b = A @ x_true

x = solve(A, b)
print("size of the residual:", f"{vnorm(residual(A, x, b), np.inf):.3e}")
print("size of the error   :", f"{vnorm(x - x_true, np.inf):.3e}")
print("largest entry of x  :", f"{np.max(x):.6f}", " (every entry should be 1)")

"""The derivative of a system is a matrix, and it can be estimated one column at a time.
"""
import numpy as np

from nmkit.nlsys import jacobian_fd

def F(v):
    x, y = v
    return np.array([x * x + y * y - 4.0, np.exp(x) + y - 1.0])

x = np.array([1.0, 1.7])
J = jacobian_fd(F, x)
print("estimated Jacobian:\n", np.array2string(J, precision=8))
exact = np.array([[2 * x[0], 2 * x[1]], [np.exp(x[0]), 1.0]])
print("exact Jacobian    :\n", np.array2string(exact, precision=8))
print("largest gap       :", f"{np.max(np.abs(J - exact)):.3e}")

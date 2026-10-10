"""The routine collects the hand steps and returns the answer to the system of Example
4.1."""
import numpy as np

from nmkit.linsolve import gauss_naive, residual

A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
b = np.array([8.0, -11.0, -3.0])

x = gauss_naive(A, b)
print("x        :", x)
print("residual :", residual(A, x, b))
print("A is unchanged by the call:\n", A)

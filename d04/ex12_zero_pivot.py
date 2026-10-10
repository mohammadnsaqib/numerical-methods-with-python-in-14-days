"""A zero on the diagonal stops elimination, although the system has a perfectly good
answer."""
import numpy as np

from nmkit.linsolve import gauss_naive, solve

A = np.array([[0.0, 1.0], [1.0, 1.0]])
b = np.array([1.0, 3.0])

print("A =\n", A, "\nb =", b)
try:
    gauss_naive(A, b)
except ZeroDivisionError as exc:
    print("gauss_naive:", exc)
print("with pivoting:", solve(A, b))
print("numpy agrees :", np.linalg.solve(A, b))

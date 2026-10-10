"""Exchanging the two rows changes nothing about the equations and everything about the
answer."""
import numpy as np

from nmkit.linsolve import gauss_naive

eps = 1e-18
A = np.array([[eps, 1.0], [1.0, 1.0]])
b = np.array([1.0, 2.0])
swapped_A = A[[1, 0], :]
swapped_b = b[[1, 0]]

print("original order:", np.array2string(gauss_naive(A, b), precision=17))
print("rows "
      "exchanged:", np.array2string(gauss_naive(swapped_A, swapped_b), precision=17))
print("numpy         :", np.array2string(np.linalg.solve(A, b), precision=17))
print("\nthe two systems have the same equations, written in a different order.")

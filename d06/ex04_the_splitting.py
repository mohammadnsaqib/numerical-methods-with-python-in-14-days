"""Every method today is one choice of which part of the matrix to invert."""
import numpy as np

from nmkit.iterative import split

A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 4.0]])
D, L, U = split(A)
print("D =\n", D)
print("L =\n", L)
print("U =\n", U)
print("\nD + L + U rebuilds A:", np.array_equal(D + L + U, A))
print("Jacobi inverts D alone; Gauss-Seidel inverts D + L.")

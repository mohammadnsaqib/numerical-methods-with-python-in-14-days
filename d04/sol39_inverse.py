"""Problem 4.39: an inverse is n systems sharing one factorisation, and it is rarely
worth it."""
import numpy as np

from nmkit.linsolve import lu_pivot, lu_solve, solve

rng = np.random.default_rng(47)
n = 6
A = rng.uniform(-3, 3, (n, n))

LU, piv, _ = lu_pivot(A)
inv = np.column_stack([lu_solve(LU, piv, np.eye(n)[:, j]) for j in range(n)])

print("largest entry of A @ inv minus the identity:",
      f"{np.max(np.abs(A @ inv - np.eye(n))):.3e}")
print("largest gap from numpy.linalg.inv        :",
      f"{np.max(np.abs(inv - np.linalg.inv(A))):.3e}")

b = rng.uniform(-3, 3, n)
print("\nsolving once by the inverse :", np.array2string(inv @ b, precision=12))
print("solving once by elimination :", np.array2string(solve(A, b), precision=12))
print("the second costs one third of the work and is the one to use.")

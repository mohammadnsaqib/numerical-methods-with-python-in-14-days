"""A square system need not have a solution, and the matrix says so before any method
runs."""
import numpy as np

singular = np.array([[1.0, 2.0], [2.0, 4.0]])       # the second row is twice the first
print("A =\n", singular)
print("determinant:", np.linalg.det(singular))

for b in (np.array([3.0, 6.0]), np.array([3.0, 7.0])):
    try:
        x = np.linalg.solve(singular, b)
        print(f"b = {b} -> {x}")
    except np.linalg.LinAlgError as exc:
        print(f"b = {b} -> refused: {exc}")

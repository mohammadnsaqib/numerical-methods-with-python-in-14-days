"""Elimination turns the matrix into a triangle by subtracting multiples of rows."""
import numpy as np

A = np.array([[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]])
b = np.array([8.0, -11.0, -3.0])

for k in range(2):
    for i in range(k + 1, 3):
        m = A[i, k] / A[k, k]
        A[i, k:] -= m * A[k, k:]
        b[i] -= m * b[k]
        print(f"row {i+1} minus {m:+.4f} times row {k+1}")
    print(np.array2string(np.column_stack([A, b]), precision=4), "\n")

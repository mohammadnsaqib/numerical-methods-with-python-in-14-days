"""Subtracting each column's shadow on the earlier ones leaves a set at right angles."""
import numpy as np

from nmkit.factor import gram_schmidt, orthogonality_error

A = np.array([[1.0, 1.0, 0.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0]])
Q, R = gram_schmidt(A)

print("Q =\n", np.array2string(Q, precision=6))
print("Q.T @ Q =\n", np.array2string(Q.T @ Q, precision=10))
print("largest gap from A:", f"{np.max(np.abs(Q @ R - A)):.3e}")
print("orthogonality error:", f"{orthogonality_error(Q):.3e}")

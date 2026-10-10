"""Problem 5.38: rescaling the rows can change the conditioning by many orders of
magnitude."""
import numpy as np

from nmkit.norms import cond

A = np.array([[1.0, 1.0], [1.0, 1.0 + 1e-6]])
badly = np.array([[1e6, 1e6], [1.0, 1.0 + 1e-6]])

print("well scaled rows :", f"{cond(A, np.inf):.4e}")
print("one row multiplied by 1e6:", f"{cond(badly, np.inf):.4e}")

# Equilibration: divide each row by its own largest entry, so no row dominates the
# others.
scaled = badly / np.max(np.abs(badly), axis=1, keepdims=True)
print("after equilibration      :", f"{cond(scaled, np.inf):.4e}")
print("\nthe three systems have the same answer; only the row scaling differs.")

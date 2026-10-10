"""A real matrix need not have real eigenvalues, and a rotation is the standard case."""
import numpy as np

rot = np.array([[0.0, -1.0], [1.0, 0.0]])            # a quarter turn
sym = np.array([[3.0, 1.0], [1.0, 3.0]])

print("a quarter turn, eigenvalues:", np.linalg.eigvals(rot))
print("a symmetric matrix         :", np.linalg.eigvals(sym))
print("\nno real direction survives a quarter turn, so no real eigenvector exists.")
print("a symmetric matrix always has real eigenvalues and orthogonal eigenvectors.")

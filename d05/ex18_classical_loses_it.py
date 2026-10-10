"""On a matrix whose columns are nearly parallel, the classical form stops being
orthogonal."""
import numpy as np

from nmkit.factor import gram_schmidt, orthogonality_error

eps = 1e-8
A = np.array([[1.0, 1.0, 1.0], [eps, 0.0, 0.0], [0.0, eps, 0.0], [0.0, 0.0, eps]])

Qc, _ = gram_schmidt(A, modified=False)
Qm, _ = gram_schmidt(A, modified=True)
print("classical Gram-Schmidt, orthogonality error:", f"{orthogonality_error(Qc):.3e}")
print("modified  Gram-Schmidt, orthogonality error:", f"{orthogonality_error(Qm):.3e}")
print("\nQ.T @ Q from the classical form:\n", np.array2string(Qc.T @ Qc, precision=8))

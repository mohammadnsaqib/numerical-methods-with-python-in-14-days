"""Reflections build a Q that stays orthogonal where subtraction did not."""
import numpy as np

from nmkit.factor import householder_qr, orthogonality_error

eps = 1e-8
A = np.array([[1.0, 1.0, 1.0], [eps, 0.0, 0.0], [0.0, eps, 0.0], [0.0, 0.0, eps]])

Q, R = householder_qr(A)
print("orthogonality error, Householder:", f"{orthogonality_error(Q[:, :3]):.3e}")
print("largest gap in Q @ R minus A    :", f"{np.max(np.abs(Q @ R - A)):.3e}")
print("R is upper triangular           :", np.allclose(R, np.triu(R)))

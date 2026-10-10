"""The square root is the test: a matrix that is not positive definite cannot be
factored."""
import numpy as np

from nmkit.factor import cholesky

cases = [
    ("positive definite", np.array([[4.0, 1.0], [1.0, 3.0]])),
    ("indefinite       ", np.array([[1.0, 3.0], [3.0, 1.0]])),
    ("negative definite", np.array([[-2.0, 0.0], [0.0, -3.0]])),
]
for name, A in cases:
    try:
        cholesky(A)
        print(f"{name}: factored, eigenvalues {np.round(np.linalg.eigvalsh(A), 4)}")
    except ValueError as exc:
        print(f"{name}: refused -- {exc}")
        print(f"{'':19}  eigenvalues {np.round(np.linalg.eigvalsh(A), 4)}")

"""Three methods for one factorisation, ranked by the only measure that separates them.
"""
import numpy as np

from nmkit.factor import gram_schmidt, householder_qr, orthogonality_error

rng = np.random.default_rng(73)
print(f"{'case':>14} {'classical':>13} {'modified':>13} {'Householder':>13} "
      f"{'numpy':>13}")
for eps in (1e-4, 1e-8, 1e-12):
    A = np.array([[1.0, 1.0, 1.0], [eps, 0.0, 0.0], [0.0, eps, 0.0], [0.0, 0.0, eps]])
    Qc, _ = gram_schmidt(A, modified=False)
    Qm, _ = gram_schmidt(A, modified=True)
    Qh, _ = householder_qr(A)
    Qn, _ = np.linalg.qr(A)
    print(f"{eps:>14.0e} {orthogonality_error(Qc):>13.2e} "
          f"{orthogonality_error(Qm):>13.2e} {orthogonality_error(Qh[:, :3]):>13.2e} "
          f"{orthogonality_error(Qn):>13.2e}")

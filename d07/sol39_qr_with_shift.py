"""Problem 7.39: one shift per step turns a first-order method into a fast one."""
import numpy as np

from nmkit.factor import householder_qr

def qr_shifted(A, tol=1e-12, max_iter=500):
    """The QR algorithm with the trailing diagonal entry used as a shift each step."""
    A = np.array(A, dtype=float, copy=True)
    n = A.shape[0]
    total = 0
    for m in range(n - 1, 0, -1):
        while total < max_iter:
            total += 1
            if abs(A[m, m - 1]) < tol:
                break
            mu = A[m, m]
            Q, R = householder_qr(A[:m + 1, :m + 1] - mu * np.eye(m + 1))
            A[:m + 1, :m + 1] = R @ Q + mu * np.eye(m + 1)
    return np.diag(A).copy(), total

for vals in ([4.0, 2.0, 1.0], [4.0, 3.8, 1.0], [4.0, 3.98, 1.0]):
    A = np.diag(vals)
    Q, _ = np.linalg.qr(np.random.default_rng(139).normal(size=(3, 3)))
    M = Q @ A @ Q.T
    got, k = qr_shifted(M)
    print(f"{str(vals):>22}: {k:>4} steps, largest gap "
          f"{np.max(np.abs(np.sort(got) - np.sort(vals))):.2e}")

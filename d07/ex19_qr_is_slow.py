"""Without a shift the QR algorithm is first order, and the ratio of neighbours sets the
rate."""
import numpy as np

from nmkit.eigen import qr_algorithm

print(f"{'eigenvalues':>22} {'closest ratio':>15} {'iterations':>12}")
for vals in ([4.0, 2.0, 1.0], [4.0, 3.0, 1.0], [4.0, 3.8, 1.0], [4.0, 3.98, 1.0]):
    A = np.diag(vals)
    Q, _ = np.linalg.qr(np.random.default_rng(109).normal(size=(3, 3)))
    M = Q @ A @ Q.T
    _, k, _ = qr_algorithm(M, tol=1e-10, max_iter=40000)
    ratio = max(vals[1] / vals[0], vals[2] / vals[1])
    print(f"{str(vals):>22} {ratio:>15.4f} {k:>12}")

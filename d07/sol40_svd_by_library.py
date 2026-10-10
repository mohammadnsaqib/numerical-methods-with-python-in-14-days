"""Problem 7.40: the two routes to a singular value, and the digits the squaring costs.
"""
import numpy as np

from nmkit.eigen import svd_from_eig

print(f"{'smallest true':>15} {'via A.T A':>14} {'via numpy':>14} "
      f"{'error, squared':>15} {'error, numpy':>14}")
for s in (1e-3, 1e-6, 1e-9, 1e-12):
    A = np.diag([1.0, 0.05, s])
    Q, _ = np.linalg.qr(np.random.default_rng(149).normal(size=(3, 3)))
    M = Q @ A @ Q.T
    mine = np.sort(svd_from_eig(M))[0]
    theirs = np.sort(np.linalg.svd(M, compute_uv=False))[0]
    print(f"{s:>15.0e} {mine:>14.4e} {theirs:>14.4e} "
          f"{abs(mine - s) / s:>15.2e} {abs(theirs - s) / s:>14.2e}")

"""Forming A transposed A squares the conditioning, so half the digits of a small value
are gone."""
import numpy as np

from nmkit.eigen import svd_from_eig

print(f"{'smallest true':>16} {'via A.T A':>16} {'relative error':>16}")
for s_small in (1e-2, 1e-4, 1e-6, 1e-8):
    A = np.diag([1.0, 0.1, s_small])
    Q, _ = np.linalg.qr(np.random.default_rng(131).normal(size=(3, 3)))
    M = Q @ A @ Q.T
    mine = np.sort(svd_from_eig(M))[0]
    print(f"{s_small:>16.0e} {mine:>16.6e} {abs(mine - s_small) / s_small:>16.3e}")
print("\nnumpy does not form A transposed A, which is why its answers keep their "
      "digits.")

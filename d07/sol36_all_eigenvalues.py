"""Problem 7.36: every eigenvalue of a symmetric matrix by power method and deflation.
"""
import numpy as np

from nmkit.eigen import deflate, power_method, residual

rng = np.random.default_rng(137)
B = rng.normal(size=(6, 6))
A = B + B.T

M, found = A.copy(), []
for _ in range(6):
    lam, v, _, _ = power_method(M, tol=1e-13, max_iter=50000)
    found.append((lam, residual(A, lam, v)))
    M = deflate(M, lam, v)

true = np.sort(np.linalg.eigvalsh(A))
print(f"{'found':>16} {'nearest true':>16} {'error':>12} {'residual vs A':>15}")
for lam, r in sorted(found, key=lambda t: t[0]):
    j = int(np.argmin(np.abs(true - lam)))
    print(f"{lam:>16.10f} {true[j]:>16.10f} {abs(lam - true[j]):>12.2e} {r:>15.2e}")

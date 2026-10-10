"""Each deflation carries the previous one's error forward, so the last value is the
worst."""
import numpy as np

from nmkit.eigen import deflate, power_method

rng = np.random.default_rng(103)
B = rng.normal(size=(5, 5))
A = B + B.T
true = np.sort(np.linalg.eigvalsh(A))[::-1]

M, found = A.copy(), []
for _ in range(5):
    lam, v, _, _ = power_method(M, tol=1e-13, max_iter=20000)
    found.append(lam)
    M = deflate(M, lam, v)

order = np.argsort(np.abs(found))[::-1]
print(f"{'step':>5} {'found':>16} {'nearest true':>16} {'error':>12}")
for i, lam in enumerate(found, 1):
    j = int(np.argmin(np.abs(true - lam)))
    print(f"{i:>5} {lam:>16.10f} {true[j]:>16.10f} {abs(lam - true[j]):>12.3e}")

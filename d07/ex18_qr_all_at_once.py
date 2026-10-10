"""Unlike the power method, one run returns every eigenvalue."""
import numpy as np

from nmkit.eigen import qr_algorithm

rng = np.random.default_rng(107)
B = rng.normal(size=(5, 5))
A = B + B.T
vals, k, _ = qr_algorithm(A, tol=1e-11, max_iter=20000)
true = np.linalg.eigvalsh(A)

print("iterations:", k)
print(f"{'from QR':>16} {'from numpy':>16} {'gap':>12}")
for a, b in zip(np.sort(vals), true):
    print(f"{a:>16.10f} {b:>16.10f} {abs(a - b):>12.2e}")

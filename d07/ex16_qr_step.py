"""One QR step: factor, then multiply the factors back in the other order."""
import numpy as np

from nmkit.factor import householder_qr

A = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
print("start:\n", np.array2string(A, precision=6))
for step in range(1, 4):
    Q, R = householder_qr(A)
    A = R @ Q
    below = np.max(np.abs(np.tril(A, -1)))
    print(f"after step {step}: largest entry below the diagonal {below:.6f}")
print("\nthe diagonal now:", np.array2string(np.diag(A), precision=8))

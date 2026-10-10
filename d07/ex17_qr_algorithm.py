"""Repeating the step drives everything below the diagonal to zero, leaving the
eigenvalues."""
import numpy as np

from nmkit.eigen import qr_algorithm

A = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
vals, k, hist = qr_algorithm(A, tol=1e-12, max_iter=5000)
print("iterations:", k)
print("from the QR algorithm:", np.array2string(np.sort(vals), precision=12))
print("from numpy           :", np.array2string(np.linalg.eigvalsh(A), precision=12))
print("largest gap          :",
      f"{np.max(np.abs(np.sort(vals) - np.linalg.eigvalsh(A))):.3e}")

"""The condition for the least-squares fit is one square system, and it can be written
down."""
import numpy as np

from nmkit.lstsq import lstsq_qr, normal_equations

A = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])
b = np.array([1.0, 3.0, 2.0])

print("A.T @ A =\n", A.T @ A)
print("A.T @ b =", A.T @ b)
print("normal equations:", np.array2string(normal_equations(A, b), precision=12))
print("through QR      :", np.array2string(lstsq_qr(A, b), precision=12))

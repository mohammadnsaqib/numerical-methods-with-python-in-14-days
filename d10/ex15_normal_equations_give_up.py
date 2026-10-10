"""At degree fourteen on forty points the normal equations return coefficients that are
not a fit."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, normal_equations, polyval
from nmkit.norms import cond

xs = np.linspace(0.0, 1.0, 40)
ys = np.exp(xs)
A = design_matrix(xs, 14)

print("condition of A     :", f"{cond(A, 2):.4e}")
print("condition of A.T A :", f"{cond(A.T @ A, 2):.4e}")
cn = normal_equations(A, ys)
cq = lstsq_qr(A, ys)
print("normal equations, largest miss:", f"{np.max(np.abs(polyval(cn, xs) - ys)):.4e}")
print("QR, largest miss              :", f"{np.max(np.abs(polyval(cq, xs) - ys)):.4e}")

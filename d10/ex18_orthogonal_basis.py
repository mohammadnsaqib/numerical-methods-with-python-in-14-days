"""Choosing a better basis is the third repair, and it beats both routes."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr, normal_equations, polyval
from nmkit.norms import cond

xs = np.linspace(0.0, 1.0, 40)
ys = np.exp(xs)
d = 14

powers = design_matrix(xs, d)
# The same space of polynomials, spanned by Legendre polynomials instead of by powers.
shifted = 2.0 * xs - 1.0
legendre = np.column_stack([np.polynomial.legendre.Legendre.basis(k)(shifted)
                            for k in range(d + 1)])

print("condition with powers   :", f"{cond(powers, 2):.4e}")
print("condition with Legendre :", f"{cond(legendre, 2):.4e}")
cl = lstsq_qr(legendre, ys)
print("Legendre basis, largest miss:", f"{np.max(np.abs(legendre @ cl - ys)):.4e}")
print("power basis with QR         :",
      f"{np.max(np.abs(polyval(lstsq_qr(powers, ys), xs) - ys)):.4e}")

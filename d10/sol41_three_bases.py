"""Problem 10.41: one space of polynomials, spanned three ways, fitted at degree
fourteen."""
import numpy as np

from nmkit.lstsq import design_matrix, lstsq_qr
from nmkit.norms import cond

xs = np.linspace(0.0, 1.0, 60)
ys = np.exp(xs)
d = 14
shifted = 2.0 * xs - 1.0

bases = {
    "powers of x": design_matrix(xs, d),
    "powers of 2x-1": design_matrix(shifted, d),
    "Legendre": np.column_stack(
        [np.polynomial.legendre.Legendre.basis(k)(shifted) for k in range(d + 1)]),
    "Chebyshev": np.column_stack(
        [np.polynomial.chebyshev.Chebyshev.basis(k)(shifted) for k in range(d + 1)]),
}

print(f"{'basis':>16} {'condition number':>19} {'largest miss':>15}")
for name, A in bases.items():
    print(f"{name:>16} {cond(A, 2):>19.4e} "
          f"{np.max(np.abs(A @ lstsq_qr(A, ys) - ys)):>15.4e}")
print("\nEvery row fits the same function with the same fourteen degrees of freedom.")
print("Only the columns differ, and the conditioning spans ten decades.")

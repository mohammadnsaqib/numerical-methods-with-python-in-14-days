"""Problem 10.37: four ways to solve one ill-conditioned fit, all judged by a 50-digit
oracle."""
import numpy as np
from mpmath import lu_solve, matrix as mpmatrix, mp, mpf

from nmkit.lstsq import design_matrix, lstsq_qr, normal_equations

mp.dps = 50
xs = np.linspace(0.0, 1.0, 40)
ys = np.exp(xs)
A = design_matrix(xs, 12)

# The oracle is given the SAME data the four routes get -- every entry of A and of ys,
# exactly as stored -- and does the whole computation at fifty digits. Forming A
# transposed A in DOUBLE and then solving it precisely would be a different problem: at
# this degree that product has already lost the answer, and no amount of later precision
# brings it back.
Am = mpmatrix([[mpf(float(v)) for v in row] for row in A])
bm = mpmatrix([mpf(float(v)) for v in ys])
exact = np.array([float(v) for v in lu_solve(Am.T * Am, Am.T * bm)])

routes = {
    "normal equations": normal_equations(A, ys),
    "our QR": lstsq_qr(A, ys),
    "numpy lstsq": np.linalg.lstsq(A, ys, rcond=None)[0],
    "pseudo-inverse": np.linalg.pinv(A) @ ys,
}
scale = np.max(np.abs(exact))
print(f"{'route':>17} {'largest coefficient error':>26}")
for name, c in routes.items():
    print(f"{name:>17} {np.max(np.abs(c - exact)) / scale:>26.3e}")

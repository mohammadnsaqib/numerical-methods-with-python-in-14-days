"""Fitting a model to more data than it has parameters. Day 10.

Interpolation passes through every point. Least squares passes through none of them, and
is the right choice whenever the data carries measurement error: forcing a curve through
noise fits the noise. The two routes here reach the same answer in exact arithmetic and
lose very different numbers of digits in floating point.
"""
import numpy as np

from .factor import householder_qr
from .linsolve import back_sub, solve


# --8<-- design_matrix
def design_matrix(xs, degree):
    """The matrix whose columns are the model's basis functions evaluated at the data.

    For a polynomial fit those are 1, x, x squared and so on. The matrix is TALL: one
    row per measurement and one column per parameter, so with more data than parameters
    there is generally no vector that satisfies every row.
    """
    xs = np.asarray(xs, dtype=float).ravel()
    return np.vander(xs, degree + 1, increasing=True)
# --8<--


# --8<-- normal_equations
def normal_equations(A, b):
    """Solve the square system A transposed A x = A transposed b.

    This is the definition made computable: it is exactly the condition that the
    residual be at right angles to every column of A. It is also the worst route,
    because forming A transposed A SQUARES the condition number, and Example 10.14
    measures the digits that costs.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).ravel()
    return solve(A.T @ A, A.T @ b)
# --8<--


# --8<-- lstsq_qr
def lstsq_qr(A, b):
    """Solve the same problem through an orthogonal factorisation instead.

    Q does not change lengths, so multiplying the residual by Q transposed changes
    nothing about its size. What is left is a triangular system in the parameters plus a
    part that no choice of parameters can touch -- and that part's size IS the smallest
    residual. The condition number is never squared.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).ravel()
    m, n = A.shape
    Q, R = householder_qr(A)
    return back_sub(R[:n, :n], (Q.T @ b)[:n])
# --8<--


def polyfit(xs, ys, degree, method="qr"):
    """Fit a polynomial of the given degree by least squares, and return its
    coefficients."""
    A = design_matrix(xs, degree)
    return lstsq_qr(A, ys) if method == "qr" else normal_equations(A, ys)


def polyval(coeffs, t):
    """Evaluate a polynomial given in increasing-power order, by Horner's rule."""
    coeffs = np.asarray(coeffs, dtype=float).ravel()
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t) + coeffs[-1]
    for c in coeffs[-2::-1]:
        out = out * t + c
    return out


# --8<-- r_squared
def r_squared(ys, fitted):
    """The share of the data's variation the model accounts for.

    One means the model passes through every point; zero means it does no better than
    the mean. It is a description of the FIT and never evidence that the model is the
    right one -- a high-degree polynomial can reach one on pure noise, which Example
    10.10 shows.
    """
    ys = np.asarray(ys, dtype=float).ravel()
    fitted = np.asarray(fitted, dtype=float).ravel()
    ss_res = float(np.sum((ys - fitted) ** 2))
    ss_tot = float(np.sum((ys - ys.mean()) ** 2))
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
# --8<--


# --8<-- weighted
def weighted(A, b, w):
    """Least squares in which each row counts as much as its weight says.

    A measurement known to ten times the precision of another should count for more, and
    the right weight is one over the square of its uncertainty. Scaling every row by the
    square root of its weight turns the weighted problem into an ordinary one, so no new
    solver is needed.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).ravel()
    s = np.sqrt(np.asarray(w, dtype=float).ravel())
    return lstsq_qr(A * s[:, None], b * s)
# --8<--


def residual(A, x, b):
    """b - A x: what the fit leaves over at every measurement."""
    A = np.asarray(A, dtype=float)
    return np.asarray(b, dtype=float).ravel() - A @ np.asarray(x, dtype=float).ravel()

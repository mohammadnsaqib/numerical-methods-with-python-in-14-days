"""Eigenvalues, eigenvectors and singular values. Day 7.

An eigenvector is a direction the matrix does not turn, only stretches, and the
eigenvalue is how much. Every method here is built from the same observation:
multiplying by the matrix again and again amplifies the direction with the largest
stretch until it is all that is left.

numpy.linalg is used as an oracle throughout and never inside a routine.
"""
import numpy as np

from .factor import householder_qr


# --8<-- power_method
def power_method(A, x0=None, tol=1e-12, max_iter=1000):
    """Multiply a vector by A over and over until it stops turning.

    Every vector is a mixture of eigenvectors. Multiplying by A multiplies each part by
    its own eigenvalue, so after k steps the largest one has grown by the largest factor
    and the mixture is dominated by its direction. The vector is rescaled every step,
    because otherwise it overflows for an eigenvalue above one and underflows for one
    below.

    Returns (eigenvalue, eigenvector, iterations, history of eigenvalue estimates).
    """
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    x = np.ones(n) if x0 is None else np.array(x0, dtype=float)
    x = x / np.sqrt(x @ x)
    lam, history = 0.0, []
    for k in range(1, max_iter + 1):
        y = A @ x
        norm = np.sqrt(y @ y)
        if norm == 0.0:
            return 0.0, x, k, history
        x_new = y / norm
        # The Rayleigh quotient rather than the ratio of two entries: it is correct even
        # when the entry a ratio would use happens to be near zero, and it converges
        # faster.
        lam_new = float(x_new @ (A @ x_new))
        history.append(lam_new)
        if abs(lam_new - lam) < tol and k > 1:
            return lam_new, x_new, k, history
        lam, x = lam_new, x_new
    return lam, x, max_iter, history
# --8<--


# --8<-- rayleigh
def rayleigh(A, x):
    """The best estimate of an eigenvalue that a given direction supports.

    For a symmetric matrix this is stationary at every eigenvector, which means an error
    of size e in the direction gives an error of size e SQUARED in the value. That is
    why it is used instead of reading one entry of A x divided by the matching entry of
    x.
    """
    A = np.asarray(A, dtype=float)
    x = np.asarray(x, dtype=float).ravel()
    return float(x @ (A @ x) / (x @ x))
# --8<--


# --8<-- inverse_iteration
def inverse_iteration(A, shift, x0=None, tol=1e-12, max_iter=200):
    """The power method on the inverse of A minus a shift, which finds the eigenvalue
    NEAREST it.

    Subtracting the shift moves the eigenvalue closest to it nearest to zero, and
    inverting then makes that one the largest. So a method that can only find the
    biggest eigenvalue finds any eigenvalue, given a guess.

    The inverse is never formed. Each step solves a system instead, which is the same
    arithmetic without the extra error, and Day 4's routine does it.
    """
    from .linsolve import lu_pivot, lu_solve

    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    x = np.ones(n) if x0 is None else np.array(x0, dtype=float)
    x = x / np.sqrt(x @ x)

    # A shift that is EXACTLY an eigenvalue makes the shifted matrix singular, and the
    # solve then fails on the first step. Returning the shift at that point looks right
    # -- the eigenvalue really is the shift -- and carries the STARTING direction, whose
    # residual was measured at 1.15 on a matrix whose other two runs gave 1e-8. The
    # eigenvalue was correct and the eigenvector was whatever it began as.
    #
    # The repair is to move the shift by a few ulps. That costs nothing in accuracy,
    # because the method converges to the eigenvalue nearest the shift and a few ulps
    # does not change which one that is, and it turns a singular solve into a very ill-
    # conditioned one -- which is exactly what makes inverse iteration converge in a
    # single step.
    M = A - shift * np.eye(n)
    scale = float(np.max(np.abs(A))) or 1.0
    nudge = 0.0
    while abs(np.linalg.det(M)) < 1e-14 * scale ** n and nudge < 1e-6 * scale:
        nudge = max(nudge * 8.0, 1e-12 * scale)
        M = A - (shift + nudge) * np.eye(n)

    LU, piv, _ = lu_pivot(M)
    lam, history = None, []
    for k in range(1, max_iter + 1):
        try:
            y = lu_solve(LU, piv, x)
        except ZeroDivisionError:
            return rayleigh(A, x), x, k, history
        norm = np.sqrt(y @ y)
        if norm == 0.0 or not np.isfinite(norm):
            return rayleigh(A, x), x, k, history
        x = y / norm
        lam_new = rayleigh(A, x)
        history.append(lam_new)
        if lam is not None and abs(lam_new - lam) < tol:
            return lam_new, x, k, history
        lam = lam_new
    return lam, x, max_iter, history
# --8<--


# --8<-- deflate
def deflate(A, lam, v):
    """Remove one eigenpair from a symmetric matrix, leaving the rest untouched.

    Subtracting the eigenvalue times the outer product of its own unit eigenvector sets
    that eigenvalue to zero and changes no other. The power method can then be run again
    to find the next largest, and repeating gives them all.

    Only valid for a SYMMETRIC matrix, whose eigenvectors are at right angles. For a
    general matrix the eigenvectors are not orthogonal and this subtraction disturbs the
    others.
    """
    v = np.asarray(v, dtype=float).ravel()
    v = v / np.sqrt(v @ v)
    return np.asarray(A, dtype=float) - lam * np.outer(v, v)
# --8<--


# --8<-- qr_algorithm
def qr_algorithm(A, tol=1e-12, max_iter=2000):
    """Factor, multiply the factors back in the other order, repeat.

    That is the whole method: A becomes R Q instead of Q R. The new matrix has the same
    eigenvalues, because it is Q transposed times A times Q, and repeating drives the
    entries below the diagonal to zero. The eigenvalues are then read off the diagonal.

    No shift is used here, so convergence is first order and slow. A shifted version is
    what a library uses; this one is written to be read.
    """
    A = np.array(A, dtype=float, copy=True)
    n = A.shape[0]
    history = []
    for k in range(1, max_iter + 1):
        Q, R = householder_qr(A)
        A = R @ Q
        below = float(np.max(np.abs(np.tril(A, -1)))) if n > 1 else 0.0
        history.append(below)
        if below < tol:
            return np.diag(A).copy(), k, history
    return np.diag(A).copy(), max_iter, history
# --8<--


# --8<-- svd_from_eig
def svd_from_eig(A):
    """The singular values, obtained as the square roots of the eigenvalues of A
    transposed A.

    This is the definition made computable, and it is deliberately NOT how a library
    does it: A transposed A squares the condition number, so a singular value near the
    format's floor comes out with half the digits. Example 7.22 measures exactly that
    loss."""
    A = np.asarray(A, dtype=float)
    vals = np.linalg.eigvalsh(A.T @ A)
    return np.sqrt(np.maximum(vals, 0.0))[::-1]
# --8<--


def residual(A, lam, v):
    """A v minus lam v: how far a claimed eigenpair is from being one.

    This is the only honest check on an eigenvalue, because the true value is generally
    not available in closed form. A small residual with a unit vector means the pair is
    right.
    """
    A = np.asarray(A, dtype=float)
    v = np.asarray(v, dtype=float).ravel()
    return float(np.max(np.abs(A @ v - lam * v)))

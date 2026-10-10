"""Factorisations that use orthogonality or symmetry instead of elimination. Day 5.

Cholesky halves the work when a matrix is symmetric and positive definite. QR costs
twice as much as LU and is stable without any pivoting at all, because an orthogonal
matrix does not change the size of what it multiplies -- which is exactly what Day 10
needs for least squares.
"""
import numpy as np


# --8<-- cholesky
def cholesky(A):
    """Factor a symmetric positive definite A into L times L transposed.

    Half the work of LU, because the symmetry means half the matrix need never be
    touched. The square root is the check: a matrix that is not positive definite
    produces a negative number under it, and that is the cheapest test for positive
    definiteness there is.
    """
    A = np.asarray(A, dtype=float)
    n = A.shape[0]
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1):
            s = float(L[i, :j] @ L[j, :j])
            if i == j:
                under = A[i, i] - s
                if under <= 0.0:
                    raise ValueError(f"not positive definite: {under:.3e} under the "
                                     f"root "
                                     f"at row {i}")
                L[i, j] = np.sqrt(under)
            else:
                L[i, j] = (A[i, j] - s) / L[j, j]
    return L
# --8<--


# --8<-- gram_schmidt
def gram_schmidt(A, modified=False):
    """Turn the columns of A into an orthonormal set, and record what was subtracted.

    The classical form subtracts, from each column, its projection onto every EARLIER
    ORIGINAL column. The modified form subtracts the projection onto each q as soon as
    that q exists, so later subtractions use a vector that has already been cleaned. In
    exact arithmetic the two are identical. In floating point they are not, and Example
    5.18 measures the difference.
    """
    A = np.asarray(A, dtype=float)
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    for j in range(n):
        v = A[:, j].copy()
        for i in range(j):
            R[i, j] = Q[:, i] @ (v if modified else A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.sqrt(v @ v)
        if R[j, j] == 0.0:
            raise ValueError(f"column {j} is a combination of the earlier ones")
        Q[:, j] = v / R[j, j]
    return Q, R
# --8<--


# --8<-- householder_qr
def householder_qr(A):
    """Factor A into Q times R using reflections rather than subtractions.

    Each step reflects one column onto a multiple of a coordinate axis, which zeroes
    everything below the diagonal in one operation. A reflection is orthogonal, so it
    changes no length and cannot magnify an error -- which is why this method needs no
    pivoting to be stable.
    """
    A = np.array(A, dtype=float, copy=True)
    m, n = A.shape
    Q = np.eye(m)
    for k in range(min(m - 1, n)):
        x = A[k:, k].copy()
        alpha = -np.sign(x[0]) * np.sqrt(x @ x) if x[0] != 0 else -np.sqrt(x @ x)
        if alpha == 0.0:
            continue
        v = x.copy()
        v[0] -= alpha
        nv = np.sqrt(v @ v)
        if nv == 0.0:
            continue
        v = v / nv
        A[k:, k:] -= 2.0 * np.outer(v, v @ A[k:, k:])
        Q[:, k:] -= 2.0 * np.outer(Q[:, k:] @ v, v)
    return Q, np.triu(A)
# --8<--


def orthogonality_error(Q):
    """How far Q transposed times Q is from the identity: the quantity that separates
    the methods.

    A method that is orthogonal on paper can lose it entirely in floating point, and
    this one number is what shows the loss. It is measured in the infinity norm, so it
    reports the worst single entry rather than an average that would hide it."""
    Q = np.asarray(Q, dtype=float)
    n = Q.shape[1]
    return float(np.max(np.abs(Q.T @ Q - np.eye(n))))

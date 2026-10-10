"""Solving a linear system by repeated improvement rather than by elimination. Day 6.

Elimination gives the answer in a fixed number of steps and fills in every zero on the
way. An iterative method never touches a zero, so a matrix with a million rows and five
entries per row is solvable when its elimination would not fit in memory. The price is
that it may not converge at all, and §6.5 gives the test.
"""
import numpy as np


def split(A):
    """A = D + L + U: the diagonal, the strictly lower part and the strictly upper part.

    Every method in this module is one choice of which pieces to invert. Naming the
    pieces once keeps the three routines readable as variations rather than as three
    separate algorithms.
    """
    A = np.asarray(A, dtype=float)
    D = np.diag(np.diag(A))
    return D, np.tril(A, -1), np.triu(A, 1)


# --8<-- spectral_radius
def spectral_radius(M):
    """The largest absolute value among a matrix's eigenvalues.

    This one number decides whether an iteration converges. Below one the error is
    multiplied by less than one at every step and dies away; above one it grows, from
    any starting guess, however good. Day 7 computes eigenvalues; here they are taken
    from the library, because the quantity is needed before the chapter that builds it.
    """
    return float(np.max(np.abs(np.linalg.eigvals(np.asarray(M, dtype=float)))))
# --8<--


# --8<-- jacobi
def jacobi(A, b, x0=None, tol=1e-10, max_iter=500):
    """Solve each equation for its own unknown, using the OLD values of all the others.

    Every entry of the new guess is computed from the previous guess alone, so the order
    of the equations does not matter and the whole sweep could be done at once. That
    independence is the method's one advantage over Gauss-Seidel, and it costs about
    twice the steps.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).ravel()
    n = b.size
    d = np.diag(A)
    if np.any(d == 0.0):
        raise ZeroDivisionError("a zero on the diagonal: reorder the equations first")
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)
    history = []
    R = A - np.diag(d)
    for k in range(1, max_iter + 1):
        nxt = (b - R @ x) / d
        step = float(np.max(np.abs(nxt - x)))
        history.append(step)
        x = nxt
        if step < tol:
            return x, k, history
    return x, max_iter, history
# --8<--


# --8<-- gauss_seidel
def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=500):
    """The same sweep, but each new value is used at once by the equations after it.

    One line differs from jacobi: the update writes into `x` rather than into a separate
    array. That single change usually halves the step count, and it makes the answer
    depend on the order the equations are written in.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).ravel()
    n = b.size
    if np.any(np.diag(A) == 0.0):
        raise ZeroDivisionError("a zero on the diagonal: reorder the equations first")
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)
    history = []
    for k in range(1, max_iter + 1):
        old = x.copy()
        for i in range(n):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i + 1:] @ x[i + 1:]) / A[i, i]
        step = float(np.max(np.abs(x - old)))
        history.append(step)
        if step < tol:
            return x, k, history
    return x, max_iter, history
# --8<--


# --8<-- sor
def sor(A, b, omega=1.0, x0=None, tol=1e-10, max_iter=500):
    """Gauss-Seidel with the step multiplied by omega, so the guess is pushed past its
    target.

    omega of 1 is exactly Gauss-Seidel. Above 1 the correction overshoots deliberately,
    which for many matrices reaches the answer in far fewer sweeps. Outside the range 0
    to 2 the iteration cannot converge at all, which is a theorem and is measured in
    Example 6.15.
    """
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float).ravel()
    n = b.size
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)
    history = []
    for k in range(1, max_iter + 1):
        old = x.copy()
        for i in range(n):
            gs = (b[i] - A[i, :i] @ x[:i] - A[i, i + 1:] @ x[i + 1:]) / A[i, i]
            x[i] = (1.0 - omega) * x[i] + omega * gs
        step = float(np.max(np.abs(x - old)))
        history.append(step)
        if not np.all(np.isfinite(x)):
            return x, k, history
        if step < tol:
            return x, k, history
    return x, max_iter, history
# --8<--


def iteration_matrix(A, method="jacobi", omega=1.0):
    """The matrix that multiplies the error at every sweep, whose spectral radius is the
    test."""
    D, L, U = split(A)
    if method == "jacobi":
        return -np.linalg.inv(D) @ (L + U)
    if method == "gauss_seidel":
        return -np.linalg.inv(D + L) @ U
    if method == "sor":
        return np.linalg.inv(D + omega * L) @ ((1 - omega) * D - omega * U)
    raise ValueError("method must be jacobi, gauss_seidel or sor")


def diagonally_dominant(A):
    """Is every diagonal entry larger than the sum of the sizes of the rest of its row?

    This is a SUFFICIENT condition for both methods to converge, and it is not
    necessary. A matrix that fails it may still converge, so a False here is not a
    verdict.
    """
    A = np.abs(np.asarray(A, dtype=float))
    d = np.diag(A)
    return bool(np.all(d > np.sum(A, axis=1) - d))

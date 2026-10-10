"""Solving a square system of linear equations by elimination. Day 4.

Everything here works on NumPy arrays but does the arithmetic itself, one entry at a
time, because the point of the chapter is what elimination DOES rather than how fast it
can be made to run. `numpy.linalg.solve` appears only as an oracle.

The routines never modify their arguments. A solver that overwrites the matrix it was
given is the correct choice in a library and the wrong one in a book, where the caller
usually wants to print the original next to the answer.
"""
import numpy as np


# --8<-- back_sub
def back_sub(U, b):
    """Solve U x = b for an upper triangular U, from the bottom row upwards.

    The last equation has one unknown, so it is solved directly. Each row above it then
    has exactly one unknown left once the values already found are substituted in. That
    is the whole method, and it is why elimination aims at a triangle in the first
    place.
    """
    U = np.asarray(U, dtype=float)
    b = np.asarray(b, dtype=float).ravel()
    n = b.size
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if U[i, i] == 0.0:
            raise ZeroDivisionError(f"zero on the diagonal at row {i}: U is singular")
        x[i] = (b[i] - U[i, i + 1:] @ x[i + 1:]) / U[i, i]
    return x
# --8<--


# --8<-- fwd_sub
def fwd_sub(L, b, unit=True):
    """Solve L y = b for a lower triangular L, from the top row downwards.

    `unit=True` means the diagonal is all ones and is not stored, which is how the LU
    factorisation below keeps L and U in a single array.
    """
    L = np.asarray(L, dtype=float)
    b = np.asarray(b, dtype=float).ravel()
    n = b.size
    y = np.zeros(n)
    for i in range(n):
        d = 1.0 if unit else L[i, i]
        if d == 0.0:
            raise ZeroDivisionError(f"zero on the diagonal at row {i}: L is singular")
        y[i] = (b[i] - L[i, :i] @ y[:i]) / d
    return y
# --8<--


# --8<-- gauss_naive
def gauss_naive(A, b):
    """Eliminate downwards without ever choosing a pivot, then substitute back.

    This is the method as it is taught by hand, and it is included so the chapter can
    show it failing. It divides by whatever entry happens to be on the diagonal: zero
    stops it, and merely small ruins the answer while stopping nothing.
    """
    A = np.array(A, dtype=float, copy=True)
    b = np.array(b, dtype=float, copy=True).ravel()
    n = b.size
    for k in range(n - 1):
        if A[k, k] == 0.0:
            raise ZeroDivisionError(f"zero pivot at step {k}: this method cannot "
                                    f"continue")
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]
    return back_sub(A, b)
# --8<--


# --8<-- lu_pivot
def lu_pivot(A):
    """Factor A into P A = L U with partial pivoting, in one array.

    Returns (LU, piv, swaps). The strict lower triangle of LU holds the multipliers of
    L, whose diagonal is all ones and is not stored; the upper triangle including the
    diagonal is U. `piv` is the row order and `swaps` counts the exchanges, which the
    determinant needs.

    The pivot is the largest available entry in the column, by size. Choosing it is the
    only difference from gauss_naive and it is the difference between a usable routine
    and a toy.
    """
    LU = np.array(A, dtype=float, copy=True)
    n = LU.shape[0]
    piv = np.arange(n)
    swaps = 0
    for k in range(n - 1):
        p = k + int(np.argmax(np.abs(LU[k:, k])))
        if LU[p, k] == 0.0:
            continue                      # the whole column is zero: A is singular
        if p != k:
            LU[[k, p], :] = LU[[p, k], :]
            piv[[k, p]] = piv[[p, k]]
            swaps += 1
        for i in range(k + 1, n):
            m = LU[i, k] / LU[k, k]
            LU[i, k] = m  # the multiplier is kept where the zero would be
            LU[i, k + 1:] -= m * LU[k, k + 1:]
    return LU, piv, swaps
# --8<--


# --8<-- lu_solve
def lu_solve(LU, piv, b):
    """Solve using a factorisation already computed, for one right-hand side.

    This is the payoff of factoring: the expensive part depends on A alone, so a second
    right hand side costs a forward and a back substitution rather than another
    elimination.
    """
    b = np.asarray(b, dtype=float).ravel()[piv]
    n = b.size
    L = np.tril(LU, -1) + np.eye(n)
    U = np.triu(LU)
    return back_sub(U, fwd_sub(L, b))
# --8<--


def solve(A, b):
    """Factor and solve in one call: the routine a reader would actually use."""
    LU, piv, _ = lu_pivot(A)
    return lu_solve(LU, piv, b)


# --8<-- det
def det(A):
    """The determinant, read off the factorisation rather than expanded.

    U's diagonal multiplied together gives the determinant up to sign, and each row
    exchange flips the sign. Expanding by minors instead costs a number of operations
    that grows like the factorial of the size, which is unusable past about ten.
    """
    LU, _, swaps = lu_pivot(A)
    return (-1.0) ** swaps * float(np.prod(np.diag(LU)))
# --8<--


def residual(A, x, b):
    """b - A x, the quantity that says whether a computed x satisfies the equations.

    Day 5 shows that a small residual does not imply a small error. It is still the
    first thing to look at, because a LARGE residual always means something is wrong.
    """
    A = np.asarray(A, dtype=float)
    return np.asarray(b, dtype=float).ravel() - A @ np.asarray(x, dtype=float).ravel()


def growth_factor(A):
    """The largest entry ever seen during elimination, divided by the largest in A.

    This is the quantity that decides whether elimination is stable. Partial pivoting
    keeps the multipliers at or below one in size, which is what stops the entries
    growing.
    """
    A = np.array(A, dtype=float, copy=True)
    n = A.shape[0]
    biggest = np.max(np.abs(A))
    start = biggest
    for k in range(n - 1):
        p = k + int(np.argmax(np.abs(A[k:, k])))
        if A[p, k] == 0.0:
            continue
        A[[k, p], :] = A[[p, k], :]
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k:] -= m * A[k, k:]
        biggest = max(biggest, float(np.max(np.abs(A))))
    return biggest / start

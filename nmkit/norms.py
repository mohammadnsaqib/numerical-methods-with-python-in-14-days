"""Measuring the size of a vector and of a matrix, and the conditioning that follows.
Day 5.

A norm turns a whole array into one non-negative number. Every error statement in this
book from here on is a statement about a norm, because "the answer is wrong" needs a
size before it means anything."""
import numpy as np


# --8<-- vnorm
def vnorm(x, p=2):
    """The size of a vector under one of the three norms this book uses.

    p=1 adds the sizes, p=2 is ordinary length, p=inf takes the largest entry. They
    differ by at most a factor of the square root of n, so a bound in one is a bound in
    all three -- but a REPORTED error must name which one it used, because a factor of n
    is not nothing.
    """
    x = np.asarray(x, dtype=float).ravel()
    if p == 1:
        return float(np.sum(np.abs(x)))
    if p == 2:
        return float(np.sqrt(np.sum(x * x)))
    if p in (np.inf, "inf"):
        return float(np.max(np.abs(x)))
    raise ValueError("p must be 1, 2 or inf")
# --8<--


# --8<-- mnorm
def mnorm(A, p=2):
    """The most a matrix can stretch any vector, measured in the matching vector norm.

    This is what "induced" means: the matrix norm is defined by the vector norm, as the
    largest ratio of output size to input size over every nonzero vector. The 1 and
    infinity norms have closed forms -- the largest column sum and the largest row sum
    -- and the 2 norm needs the largest singular value, which Day 7 computes.
    """
    A = np.asarray(A, dtype=float)
    if p == 1:
        return float(np.max(np.sum(np.abs(A), axis=0)))
    if p in (np.inf, "inf"):
        return float(np.max(np.sum(np.abs(A), axis=1)))
    if p == 2:
        return float(np.max(np.linalg.svd(A, compute_uv=False)))
    if p == "fro":
        return float(np.sqrt(np.sum(A * A)))
    raise ValueError("p must be 1, 2, inf or 'fro'")
# --8<--


# --8<-- cond
def cond(A, p=2):
    """How much a relative change in the data can be amplified in the answer.

    For a square matrix it is the norm of A times the norm of its inverse, which is the
    definition and is computed that way here because the definition is what Day 5 is
    about.

    A RECTANGULAR matrix has a condition number too, and the definition above cannot
    reach it: there is no inverse to form. Day 10 needs exactly that -- a design matrix
    is tall by construction -- and the first version of this routine returned infinity
    for every one of them, which read as an answer rather than as a refusal. The general
    definition is the largest singular value over the smallest, which agrees with the
    inverse form wherever both apply and is what Day 7 built.
    """
    A = np.asarray(A, dtype=float)
    if A.shape[0] != A.shape[1] or p != 2:
        s = np.linalg.svd(A, compute_uv=False)
        return float("inf") if s[-1] == 0.0 else float(s[0] / s[-1])
    try:
        inv = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return float("inf")
    return mnorm(A, p) * mnorm(inv, p)
# --8<--


# --8<-- digits_lost
def digits_lost(A, p=2):
    """The decimal digits a solve with this matrix can give away, before it is run.

    This is the base-ten logarithm of the condition number. Subtracting it from the
    format's sixteen digits gives what may be left, and a value at or above sixteen
    means no digit of the answer is guaranteed.
    """
    k = cond(A, p)
    return float("inf") if not np.isfinite(k) else float(np.log10(k))
# --8<--


def hilbert(n):
    """The Hilbert matrix: entry (i, j) is 1 / (i + j + 1).

    It is the standard specimen of an ill-conditioned matrix, and it is not artificial:
    it is what the normal equations produce when a polynomial is fitted on [0, 1], which
    is exactly what Day 10 does.
    """
    i = np.arange(n)
    return 1.0 / (i[:, None] + i[None, :] + 1.0)

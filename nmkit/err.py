"""Absolute error, relative error, significant digits, and the tables that report them.
Day 1.

Every later chapter measures itself with these four routines, so they are written once
and never re-derived. The true value they are given is always an oracle value: an exact
symbolic result, or one carried to fifty digits by mpmath, never a second float."""
import math


# --8<-- errors
def abs_err(approx, true):
    """The size of the difference between a computed value and the true value."""
    return abs(float(approx) - float(true))


def rel_err(approx, true):
    """The absolute error divided by the size of the true value.

    Relative error is the one that travels: it means the same thing at 1e-9 and at 1e9,
    which absolute error does not. When the true value is zero there is no relative
    error to report, and returning a large sentinel would hide that, so this raises
    instead.
    """
    t = float(true)
    if t == 0.0:
        raise ValueError("relative error is undefined against a true value of zero")
    return abs(float(approx) - t) / abs(t)
# --8<--


# --8<-- sig_digits
def sig_digits(approx, true):
    """How many decimal digits of `approx` agree with `true`.

    A relative error of 10 ** -k means about k correct digits, so the count is the
    negative base-ten logarithm of the relative error. An identical pair has every digit
    right and is reported as the working precision rather than as infinity.
    """
    r = rel_err(approx, true)
    if r == 0.0:
        return 16.0
    return -math.log10(r)
# --8<--


def error_table(pairs, true, labels=None):
    """Rows of (label, value, absolute error, relative error) against one true value.

    `pairs` is a sequence of computed values. The table is the book's standard way of
    showing that a method improves, and printing both errors side by side is deliberate:
    a falling absolute error on a shrinking quantity can hide a relative error that is
    not falling.
    """
    labels = labels or [str(i) for i in range(len(pairs))]
    rows = []
    for lab, v in zip(labels, pairs):
        rows.append((lab, float(v), abs_err(v, true), rel_err(v, true)))
    return rows


def print_error_table(rows, head=("n", "value", "abs err", "rel err")):
    """Print the rows of error_table in fixed columns."""
    print(f"{head[0]:>6} {head[1]:>22} {head[2]:>12} {head[3]:>12}")
    for lab, v, a, r in rows:
        print(f"{lab:>6} {v:>22.15e} {a:>12.3e} {r:>12.3e}")


# --8<-- ratio_table
def ratio_table(errors):
    """Successive ratios of a sequence of errors.

    The ratio is what tells a method's order apart from a claim about it. A ratio that
    settles on a constant below one is first order. A ratio that itself falls by the
    same factor each step is second order or better, and Day 3 measures the exponent
    directly.
    """
    out = []
    for a, b in zip(errors, errors[1:]):
        out.append(b / a if a != 0 else float("nan"))
    return out
# --8<--

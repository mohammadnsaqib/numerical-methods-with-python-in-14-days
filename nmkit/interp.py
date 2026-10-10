"""Constructing a polynomial that passes exactly through given points. Day 8.

Three forms of the same polynomial appear here. They are equal as functions and differ
entirely in what they cost to build, what they cost to evaluate, and how much accuracy
they lose -- which is the whole lesson of the chapter.
"""
import numpy as np


# --8<-- vandermonde_fit
def vandermonde_fit(xs, ys):
    """The coefficients of the interpolating polynomial, by solving a linear system.

    Row i of the matrix is 1, x, x squared and so on, so the system says "this
    polynomial takes value y at x" once per point. It is the definition made computable,
    and it is the worst of the three routes: the matrix is famously ill-conditioned, and
    Example 8.6 measures how quickly it becomes useless.
    """
    xs = np.asarray(xs, dtype=float).ravel()
    n = xs.size
    V = np.vander(xs, n, increasing=True)
    return np.linalg.solve(V, np.asarray(ys, dtype=float).ravel())
# --8<--


def vandermonde_matrix(xs):
    """The matrix itself, so a chapter can measure its conditioning."""
    xs = np.asarray(xs, dtype=float).ravel()
    return np.vander(xs, xs.size, increasing=True)


# --8<-- lagrange_eval
def lagrange_eval(xs, ys, t):
    """Evaluate the interpolating polynomial without ever finding its coefficients.

    Each basis function is 1 at its own node and 0 at every other, so the sum of y times
    basis passes through every point by construction. Nothing is solved and nothing can
    be ill-conditioned -- but every evaluation costs the whole product again, and adding
    a point means starting over.
    """
    xs = np.asarray(xs, dtype=float).ravel()
    ys = np.asarray(ys, dtype=float).ravel()
    t = np.atleast_1d(np.asarray(t, dtype=float))
    out = np.zeros_like(t)
    for i in range(xs.size):
        term = np.ones_like(t) * ys[i]
        for j in range(xs.size):
            if i != j:
                term = term * (t - xs[j]) / (xs[i] - xs[j])
        out = out + term
    return out if out.size > 1 else float(out[0])
# --8<--


# --8<-- divided_differences
def divided_differences(xs, ys):
    """The table whose top row is the Newton form's coefficients.

    Entry (i, j) is the divided difference over points i through i+j. The first column
    is the values themselves; each later column divides a difference of the column
    before it by the span of x it covers. The top row is what the Newton form needs.

    Adding one point appends one row and one entry, and every earlier coefficient is
    unchanged. That is the property neither of the other two forms has.
    """
    xs = np.asarray(xs, dtype=float).ravel()
    n = xs.size
    T = np.zeros((n, n))
    T[:, 0] = np.asarray(ys, dtype=float).ravel()
    for j in range(1, n):
        for i in range(n - j):
            T[i, j] = (T[i + 1, j - 1] - T[i, j - 1]) / (xs[i + j] - xs[i])
    return T
# --8<--


# --8<-- newton_eval
def newton_eval(xs, coeffs, t):
    """Evaluate the Newton form, innermost bracket outwards.

    Written this way the whole polynomial costs one multiply and one add per point,
    which is the same as Horner's rule and the cheapest evaluation available. The nested
    form also avoids ever computing a large power of t, which is where the coefficient
    form loses digits.
    """
    xs = np.asarray(xs, dtype=float).ravel()
    coeffs = np.asarray(coeffs, dtype=float).ravel()
    t = np.atleast_1d(np.asarray(t, dtype=float))
    out = np.full_like(t, coeffs[-1])
    for k in range(coeffs.size - 2, -1, -1):
        out = out * (t - xs[k]) + coeffs[k]
    return out if out.size > 1 else float(out[0])
# --8<--


# --8<-- chebyshev_nodes
def chebyshev_nodes(a, b, n):
    """n points spaced so that the interpolation error is as small as it can be made.

    They are the projections onto the interval of points spaced evenly round a
    semicircle, so they crowd towards the ends -- which is exactly where equal spacing
    fails. The choice is not a heuristic: these nodes minimise the largest value of the
    product that appears in the error term of §8.6, and no other choice of n points does
    better.
    """
    k = np.arange(n)
    unit = np.cos((2.0 * k + 1.0) * np.pi / (2.0 * n))
    return 0.5 * (a + b) + 0.5 * (b - a) * unit[::-1]
# --8<--


def error_product(xs, t):
    """The product of (t - x) over every node: the part of the error term a method
    controls.

    The error at t is this product, times a derivative of the function, divided by a
    factorial. Only the product depends on where the nodes were put, so it is the only
    part any choice of nodes can improve.
    """
    xs = np.asarray(xs, dtype=float).ravel()
    t = np.atleast_1d(np.asarray(t, dtype=float))
    out = np.ones_like(t)
    for x in xs:
        out = out * (t - x)
    return out


def runge(x):
    """1 / (1 + 25 x squared): the standard function on which equal spacing fails."""
    x = np.asarray(x, dtype=float)
    return 1.0 / (1.0 + 25.0 * x * x)

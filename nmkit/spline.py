"""Piecewise polynomials: low degree on many pieces, instead of high degree on one. Day
9.

Day 8 ended with a polynomial of degree twenty-four oscillating wildly between its
nodes. A spline never raises the degree at all: it uses a cubic on every interval and
joins them so that the joins cannot be seen. Adding points then adds pieces rather than
degree, and the Runge phenomenon has nothing to grow in."""
import numpy as np


# --8<-- thomas
def thomas(lower, diag, upper, rhs):
    """Solve a tridiagonal system in one forward pass and one backward pass.

    Only the entry directly below each pivot is nonzero, so an elimination step touches
    two numbers rather than a whole submatrix. The cost falls from n cubed to n, which
    is what makes a spline through ten thousand points possible.

    No pivoting is done. For the systems this book builds that is safe, because the
    matrix is diagonally dominant by construction -- the diagonal is twice the sum of
    the two neighbours for equally spaced points, and more than their sum for any
    spacing.
    """
    n = len(diag)
    c = np.array(upper, dtype=float)
    d = np.array(rhs, dtype=float)
    b = np.array(diag, dtype=float)
    a = np.asarray(lower, dtype=float)
    for i in range(1, n):
        m = a[i - 1] / b[i - 1]
        b[i] -= m * c[i - 1]
        d[i] -= m * d[i - 1]
    x = np.zeros(n)
    x[-1] = d[-1] / b[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]
    return x
# --8<--


# --8<-- cubic_spline
def cubic_spline(xs, ys, bc="natural", slopes=None):
    """The second derivatives at the knots, from which every piece's cubic follows.

    A cubic on each of n-1 intervals has 4(n-1) unknowns. Passing through the data gives
    2(n-1) conditions, matching first derivatives at the interior knots gives n-2, and
    matching second derivatives another n-2. That is two short, and the two end
    conditions supply them.

    `bc="natural"` sets the second derivative to zero at both ends. `bc="clamped"` sets
    the FIRST derivative to given values instead, which needs those values but
    reproduces the function far better near the ends -- Example 9.16 measures the
    difference.
    """
    xs = np.asarray(xs, dtype=float).ravel()
    ys = np.asarray(ys, dtype=float).ravel()
    n = xs.size
    if n < 3:
        raise ValueError("a cubic spline needs at least three points")
    h = np.diff(xs)
    if np.any(h <= 0):
        raise ValueError("the nodes must be strictly increasing")

    diag = np.empty(n)
    lower = np.empty(n - 1)
    upper = np.empty(n - 1)
    rhs = np.zeros(n)
    for i in range(1, n - 1):
        lower[i - 1] = h[i - 1]
        diag[i] = 2.0 * (h[i - 1] + h[i])
        upper[i] = h[i]
        rhs[i] = 6.0 * ((ys[i + 1] - ys[i]) / h[i] - (ys[i] - ys[i - 1]) / h[i - 1])

    if bc == "natural":
        diag[0] = diag[-1] = 1.0
        upper[0] = lower[-1] = 0.0
        rhs[0] = rhs[-1] = 0.0
    elif bc == "clamped":
        if slopes is None:
            raise ValueError("clamped ends need the two end slopes")
        diag[0] = 2.0 * h[0]
        upper[0] = h[0]
        rhs[0] = 6.0 * ((ys[1] - ys[0]) / h[0] - slopes[0])
        lower[-1] = h[-1]
        diag[-1] = 2.0 * h[-1]
        rhs[-1] = 6.0 * (slopes[1] - (ys[-1] - ys[-2]) / h[-1])
    else:
        raise ValueError("bc must be 'natural' or 'clamped'")
    return thomas(lower, diag, upper, rhs)
# --8<--


# --8<-- spline_eval
def spline_eval(xs, ys, m, t):
    """Evaluate the spline whose second derivatives at the knots are m.

    The interval is found by a binary search, so evaluating at one point costs the
    logarithm of the count of knots rather than a pass over all of them. That is the
    second reason a spline scales where a single polynomial does not.
    """
    xs = np.asarray(xs, dtype=float).ravel()
    ys = np.asarray(ys, dtype=float).ravel()
    m = np.asarray(m, dtype=float).ravel()
    t = np.atleast_1d(np.asarray(t, dtype=float))
    i = np.clip(np.searchsorted(xs, t) - 1, 0, xs.size - 2)
    h = xs[i + 1] - xs[i]
    a = xs[i + 1] - t
    b = t - xs[i]
    out = (m[i] * a ** 3 + m[i + 1] * b ** 3) / (6.0 * h) \
        + (ys[i] / h - m[i] * h / 6.0) * a \
        + (ys[i + 1] / h - m[i + 1] * h / 6.0) * b
    return out if out.size > 1 else float(out[0])
# --8<--


def piecewise_linear(xs, ys, t):
    """Join the points with straight lines: the simplest piecewise interpolant there is.
    """
    return np.interp(np.asarray(t, dtype=float), np.asarray(xs, dtype=float),
                     np.asarray(ys, dtype=float))


# --8<-- pchip_slopes
def pchip_slopes(xs, ys):
    """End slopes chosen so the interpolant never overshoots the data.

    A cubic spline is smooth and can rise above every value it was given, which for a
    quantity that cannot be negative is a wrong answer rather than an inelegant one.
    This rule sets each interior slope to a harmonic mean of the two neighbouring
    secants, and to zero wherever they disagree in sign -- which is exactly where an
    overshoot would begin.
    """
    xs = np.asarray(xs, dtype=float).ravel()
    ys = np.asarray(ys, dtype=float).ravel()
    n = xs.size
    h = np.diff(xs)
    delta = np.diff(ys) / h
    d = np.zeros(n)
    for i in range(1, n - 1):
        if delta[i - 1] * delta[i] <= 0.0:
            d[i] = 0.0  # a turning point: a flat slope cannot overshoot
        else:
            w1, w2 = 2.0 * h[i] + h[i - 1], h[i] + 2.0 * h[i - 1]
            d[i] = (w1 + w2) / (w1 / delta[i - 1] + w2 / delta[i])
    d[0] = _end_slope(h[0], h[1], delta[0], delta[1]) if n > 2 else delta[0]
    d[-1] = _end_slope(h[-1], h[-2], delta[-1], delta[-2]) if n > 2 else delta[-1]
    return d


def _end_slope(h0, h1, d0, d1):
    """The end slope, by the one-sided three-point rule with the two limiters.

    Setting the end slope to the first secant is the obvious choice and it is WRONG: it
    makes the end piece disagree with every standard implementation, by up to 0.4 on
    data of size 1, which is a disagreement of method rather than of rounding. The rule
    below fits a parabola through the first three points, then applies two limits --
    flatten if the slope points the wrong way, and cap at three secants if the data
    turns just inside the end. Both limits exist to stop the very overshoot this whole
    routine is for.
    """
    s = ((2.0 * h0 + h1) * d0 - h0 * d1) / (h0 + h1)
    if s * d0 <= 0.0:
        return 0.0
    if d0 * d1 <= 0.0 and abs(s) > 3.0 * abs(d0):
        return 3.0 * d0
    return s
# --8<--


def hermite_eval(xs, ys, d, t):
    """Evaluate the piecewise cubic with given values and given slopes at the knots."""
    xs = np.asarray(xs, dtype=float).ravel()
    ys = np.asarray(ys, dtype=float).ravel()
    d = np.asarray(d, dtype=float).ravel()
    t = np.atleast_1d(np.asarray(t, dtype=float))
    i = np.clip(np.searchsorted(xs, t) - 1, 0, xs.size - 2)
    h = xs[i + 1] - xs[i]
    s = (t - xs[i]) / h
    h00 = 2 * s ** 3 - 3 * s ** 2 + 1
    h10 = s ** 3 - 2 * s ** 2 + s
    h01 = -2 * s ** 3 + 3 * s ** 2
    h11 = s ** 3 - s ** 2
    out = h00 * ys[i] + h10 * h * d[i] + h01 * ys[i + 1] + h11 * h * d[i + 1]
    return out if out.size > 1 else float(out[0])

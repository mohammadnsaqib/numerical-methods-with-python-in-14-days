"""Estimating a definite integral from values of the integrand. Day 12.

Day 11 was the day a smaller step stopped helping. Integration is the opposite case and
it is worth saying why: a quadrature rule ADDS values rather than subtracting them, so
nothing cancels and there is no round-off floor to run into. Halving the spacing keeps
paying, all the way down to the point where the sum's own rounding accumulates -- which
takes millions of terms.
"""
import numpy as np


# --8<-- trapezoid
def trapezoid(f, a, b):
    """The area under the straight line joining the two endpoints.

    It is the crudest rule that is not a guess, and it is exact for any straight line.
    Its error is proportional to the cube of the width, which sounds strong and is not:
    one panel across a wide interval is still one straight line.
    """
    return (b - a) * (f(a) + f(b)) / 2.0
# --8<--


# --8<-- simpson
def simpson(f, a, b):
    """The area under the parabola through the two endpoints and the midpoint.

    One extra evaluation buys two orders rather than one. The parabola's own symmetry
    kills the cubic term as well as the quadratic, so the rule is exact for every
    polynomial up to degree three -- a fact Example 12.13 checks rather than asserts.
    """
    m = (a + b) / 2.0
    return (b - a) * (f(a) + 4.0 * f(m) + f(b)) / 6.0
# --8<--


# --8<-- composite
def composite(rule, f, a, b, n):
    """Apply a rule on n panels and add the results.

    This is what makes a local rule useful. The error of one panel is proportional to a
    power of the panel width, and there are n panels, so their errors add and one power
    of n is lost. A rule single-panel error goes like h**3 gives a composite error going
    like h**2.
    """
    edges = np.linspace(a, b, n + 1)
    return float(sum(rule(f, edges[i], edges[i + 1]) for i in range(n)))
# --8<--


# --8<-- trapezoid_n
def trapezoid_n(f, a, b, n):
    """The composite trapezoidal rule, written as one weighted sum rather than n calls.

    The interior points are shared between neighbouring panels, so each is counted once
    with weight one rather than twice with weight one half. That halves the evaluations
    and is the form every library uses.
    """
    x = np.linspace(a, b, n + 1)
    y = np.asarray([f(t) for t in x], dtype=float)
    h = (b - a) / n
    return float(h * (y[0] / 2.0 + y[1:-1].sum() + y[-1] / 2.0))
# --8<--


# --8<-- simpson_n
def simpson_n(f, a, b, n):
    """The composite Simpson rule on n panels, where n must be even.

    The alternating weights 4 and 2 are not decoration: they come from adding
    overlapping parabolas, each spanning two panels. An odd n has no such pairing, so
    the routine refuses rather than quietly using a different rule.
    """
    if n % 2 != 0:
        raise ValueError("Simpson's rule needs an even count of panels")
    x = np.linspace(a, b, n + 1)
    y = np.asarray([f(t) for t in x], dtype=float)
    h = (b - a) / n
    return float(h / 3.0 * (y[0] + 4.0 * y[1:-1:2].sum()
                            + 2.0 * y[2:-1:2].sum() + y[-1]))
# --8<--


# --8<-- romberg
def romberg(f, a, b, levels=6):
    """Richardson extrapolation applied to the trapezoidal rule.

    Day 11 built the table; this fills it with areas instead of slopes. The trapezoidal
    rule's error contains only EVEN powers of h, so the terms are two apart and each
    column gains two orders: column 1 IS Simpson's rule, and column 2 is better than any
    rule this book names.
    """
    T = np.zeros((levels, levels))
    for i in range(levels):
        T[i, 0] = trapezoid_n(f, a, b, 2 ** i)
        for j in range(1, i + 1):
            T[i, j] = T[i, j - 1] + (T[i, j - 1] - T[i - 1, j - 1]) / (4.0 ** j - 1.0)
    return T
# --8<--


# --8<-- gauss_legendre
def gauss_legendre(f, a, b, n):
    """Choose the POINTS as well as the weights, and n of them integrate degree 2n-1
    exactly.

    Every rule so far fixed the points on a grid and solved for weights. Freeing the
    points doubles what the same count of evaluations can do. The nodes are the roots of
    the nth Legendre polynomial, which is why the basis of Day 10 returns here.
    """
    x, w = np.polynomial.legendre.leggauss(n)
    t = 0.5 * (b - a) * x + 0.5 * (a + b)
    return float(0.5 * (b - a) * np.sum(w * np.asarray([f(v) for v in t], dtype=float)))
# --8<--


# --8<-- adaptive_simpson
def adaptive_simpson(f, a, b, tol=1e-10, depth=50):
    """Spend panels where the integrand needs them and nowhere else.

    One Simpson estimate over a panel is compared with two over its halves. Their
    difference estimates the error, and a panel that already meets its share of the
    tolerance is not split again. A peak a thousandth of the interval wide then costs a
    handful of panels, not a grid fine enough to resolve it everywhere.
    """
    calls = [0]

    def g(t):
        calls[0] += 1
        return f(t)

    def step(lo, hi, whole, k):
        mid = (lo + hi) / 2.0
        left, right = simpson(g, lo, mid), simpson(g, mid, hi)
        if k <= 0 or abs(left + right - whole) <= 15.0 * tol:
            return left + right + (left + right - whole) / 15.0
        return step(lo, mid, left, k - 1) + step(mid, hi, right, k - 1)

    total = step(a, b, simpson(g, a, b), depth)
    return total, calls[0]
# --8<--


def midpoint(f, a, b):
    """The area of the rectangle whose height is the value at the middle.

    It uses one evaluation rather than two and has the same order as the trapezoidal
    rule, with an error half the size and the OPPOSITE sign. Two parts midpoint to one
    part trapezoidal therefore cancels the leading error of both, and that combination
    is Simpson's rule -- which Example 12.11 checks by computing it three ways.
    """
    return (b - a) * f((a + b) / 2.0)

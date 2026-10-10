"""Problems whose conditions are given at BOTH ends of the interval. Day 14.

An initial value problem hands over everything at one instant, so a method can march
forward from it. A boundary value problem gives half the information at each end, and
marching is no longer possible: the start is not fully known until the finish comes out
right.

The two routines here are the two answers to that. One turns the problem back into an
initial value problem and hunts for the missing start. The other refuses to march at all
and solves for every point of the solution at once.
"""
import numpy as np

from .linsolve import solve
from .ode import rk4
from .roots import secant


# --8<-- shoot
def shoot(f, a, b, alpha, beta, guess0, guess1, n=200, tol=1e-12, max_iter=60):
    """Guess the missing slope at the left end, integrate, and correct the guess.

    The whole boundary value problem collapses into ONE equation in ONE unknown: the
    value at the right end, as a function of the slope tried at the left, must equal
    beta. Day 2's root finders solve it. Nothing new is needed, which is the point.

    The returned miss is the value of that equation at the answer, and the count of
    secant steps comes back with it, so a reader can see that the root was actually
    found rather than merely returned.
    """
    def endpoint(s):
        """Where the trajectory launched with slope s lands at b."""
        _, ys = rk4(f, a, [alpha, s], (b - a) / n, n)
        return float(ys[-1, 0]) - beta

    found = secant(endpoint, guess0, guess1, tol=tol, max_iter=max_iter)
    s = float(found.root)
    ts, ys = rk4(f, a, [alpha, s], (b - a) / n, n)
    return ts, ys, s, abs(endpoint(s)), found.iterations
# --8<--


# --8<-- fd_bvp
def fd_bvp(p, q, r, a, b, alpha, beta, n):
    """Solve y'' = p(x) y' + q(x) y + r(x) by replacing every derivative with a
    difference.

    Day 11's centred formulas turn the equation at each interior point into one linear
    equation in three unknown values. There are n-1 interior points and n-1 unknowns,
    and the matrix is TRIDIAGONAL -- which is Day 9's Thomas algorithm, arriving from a
    different direction.

    Nothing is marched. Every value is found at once, so a bad guess cannot send the
    solution to infinity the way Example 14.17 shows shooting can."""
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    m = n - 1
    A = np.zeros((m, m))
    rhs = np.zeros(m)
    for i in range(m):
        xi = x[i + 1]
        A[i, i] = 2.0 + h * h * q(xi)
        if i > 0:
            A[i, i - 1] = -1.0 - h * p(xi) / 2.0
        if i < m - 1:
            A[i, i + 1] = -1.0 + h * p(xi) / 2.0
        rhs[i] = -h * h * r(xi)
    rhs[0] += (1.0 + h * p(x[1]) / 2.0) * alpha
    rhs[-1] += (1.0 - h * p(x[m]) / 2.0) * beta
    y = np.empty(n + 1)
    y[0], y[-1] = alpha, beta
    y[1:-1] = solve(A, rhs)
    return x, y
# --8<--


# --8<-- fd_matrix
def fd_matrix(p, q, a, b, n):
    """The matrix of the finite difference system, returned rather than solved.

    It is here so a chapter can MEASURE what Day 5 predicted about it: the condition
    number of this matrix grows like the square of the count of points, so halving the
    spacing quadruples the digits at risk while the truncation error falls by four.
    Example 14.19 finds where those two meet.
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    m = n - 1
    A = np.zeros((m, m))
    for i in range(m):
        xi = x[i + 1]
        A[i, i] = 2.0 + h * h * q(xi)
        if i > 0:
            A[i, i - 1] = -1.0 - h * p(xi) / 2.0
        if i < m - 1:
            A[i, i + 1] = -1.0 + h * p(xi) / 2.0
    return A
# --8<--

"""Systems of nonlinear equations: several unknowns, several equations, none of them
linear. Day 6.

Day 3 solved one equation in one unknown. The generalisation replaces the derivative
with a matrix of partial derivatives and the division by a linear solve, and every other
part of Newton's method is unchanged -- including its second order and its lack of any
guarantee.
"""
import numpy as np

from .linsolve import solve


# --8<-- jacobian_fd
def jacobian_fd(F, x, h=None):
    """The matrix of partial derivatives, estimated by moving one variable at a time.

    Column j is how the whole output moves when input j moves. The step is scaled to the
    size of the variable it perturbs, because a fixed absolute step is too large for a
    variable near 1e6 and lands inside the rounding for one near 1e-6.

    A central difference costs twice the evaluations of a forward one and is worth it
    here: the error falls as the square of the step rather than as the step, which Day
    11 measures.
    """
    x = np.asarray(x, dtype=float).ravel()
    n = x.size
    f0 = np.asarray(F(x), dtype=float).ravel()
    J = np.zeros((f0.size, n))
    for j in range(n):
        step = h if h is not None else 1e-6 * max(abs(x[j]), 1.0)
        up, dn = x.copy(), x.copy()
        up[j] += step
        dn[j] -= step
        J[:, j] = (np.asarray(F(up), dtype=float).ravel()
                   - np.asarray(F(dn), dtype=float).ravel()) / (2.0 * step)
    return J
# --8<--


# --8<-- newton_system
def newton_system(F, x0, J=None, tol=1e-12, max_iter=60):
    """Newton's method with the derivative replaced by a matrix and the division by a
    solve.

    Each step solves J s = -F(x) and adds s to x. The solve is Day 4's, with pivoting,
    so a badly ordered Jacobian costs nothing. Returns (x, iterations, history of step
    sizes).
    """
    x = np.asarray(x0, dtype=float).ravel().copy()
    history = []
    for k in range(1, max_iter + 1):
        Fx = np.asarray(F(x), dtype=float).ravel()
        Jx = jacobian_fd(F, x) if J is None else np.asarray(J(x), dtype=float)
        try:
            s = solve(Jx, -Fx)
        except (ZeroDivisionError, np.linalg.LinAlgError):
            return x, k, history
        x = x + s
        history.append(float(np.max(np.abs(s))))
        if history[-1] < tol:
            return x, k, history
    return x, max_iter, history
# --8<--


# --8<-- broyden
def broyden(F, x0, tol=1e-12, max_iter=100):
    """Newton's method with the Jacobian UPDATED rather than recomputed.

    A Jacobian by finite difference costs 2n evaluations of F every step. Broyden's
    method pays that once, then adjusts the matrix using only the step just taken and
    the change in F it produced. The order drops below two and the cost per step drops
    by a factor of n, and Example 6.22 measures which wins.
    """
    x = np.asarray(x0, dtype=float).ravel().copy()
    B = jacobian_fd(F, x)
    Fx = np.asarray(F(x), dtype=float).ravel()
    history = []
    for k in range(1, max_iter + 1):
        try:
            s = solve(B, -Fx)
        except (ZeroDivisionError, np.linalg.LinAlgError):
            return x, k, history
        x = x + s
        Fn = np.asarray(F(x), dtype=float).ravel()
        y = Fn - Fx
        denom = float(s @ s)
        if denom > 0.0:
            B = B + np.outer(y - B @ s, s) / denom
        Fx = Fn
        history.append(float(np.max(np.abs(s))))
        if history[-1] < tol:
            return x, k, history
    return x, max_iter, history
# --8<--


def count_calls(F):
    """Wrap F so it counts how many times it is evaluated.

    Step counts are the wrong currency for comparing these two methods: a Newton step
    costs 2n+1 evaluations and a Broyden step costs 1. Counting the evaluations is what
    makes the comparison in Example 6.22 mean anything.
    """
    state = {"n": 0}

    def wrapped(x):
        state["n"] += 1
        return F(x)

    wrapped.count = lambda: state["n"]
    return wrapped

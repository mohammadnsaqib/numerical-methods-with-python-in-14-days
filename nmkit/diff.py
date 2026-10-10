"""Estimating a derivative from values of a function. Day 11.

This is the first method in the book where making the step smaller stops helping. Every
other day's error falls as the work rises. Here two errors move in opposite directions
-- the formula's own error falls with the step, and the subtraction's error rises as the
step shrinks -- so there is a step that is best and steps on either side of it that are
worse."""
import numpy as np


# --8<-- forward_diff
def forward_diff(f, x, h):
    """The slope of the line through (x, f(x)) and (x + h, f(x + h)).

    This is the definition of the derivative with the limit left out. Its error is
    proportional to h, so halving the step halves the error -- until the subtraction in
    the numerator starts cancelling, which Example 11.11 measures."""
    return (f(x + h) - f(x)) / h
# --8<--


# --8<-- backward_diff
def backward_diff(f, x, h):
    """The same line, drawn to the left instead of the right.

    It has the same order and the same weaknesses. It exists because the point to the
    right is sometimes not available: the end of a table, or the present moment in a
    measured signal."""
    return (f(x) - f(x - h)) / h
# --8<--


# --8<-- central_diff
def central_diff(f, x, h):
    """The slope of the line through the two points on either side of x.

    The first-order terms of the two one-sided errors have opposite signs and cancel,
    leaving an error proportional to h squared. That is the whole reason to prefer it:
    at the same step it is more accurate, and at a tenth of the step it is a hundred
    times more accurate."""
    return (f(x + h) - f(x - h)) / (2.0 * h)
# --8<--


# --8<-- second_diff
def second_diff(f, x, h):
    """The second derivative, from three values and one step.

    The numerator is a difference of differences, which is where the trouble is: for
    small h the three values agree to many digits and subtracting them twice throws most
    of those digits away. The round-off here grows like one over h squared, not one over
    h."""
    return (f(x + h) - 2.0 * f(x) + f(x - h)) / (h * h)
# --8<--


# --8<-- best_step
def best_step(order=2, scale=1.0):
    """The step that balances the formula's error against the subtraction's, before
    running.

    Balancing an error of size h**p against one of size eps/h gives h proportional to
    the (p+1)th root of eps. For the centred difference that is the cube root of the
    machine epsilon, near 6e-06 -- not the smallest step available, and not close to it.
    """
    eps = float(np.finfo(float).eps)
    return float(scale * eps ** (1.0 / (order + 1)))
# --8<--


# --8<-- richardson
def richardson(estimate, x, h, order=2, gap=2, levels=4):
    """Combine estimates at h, h/2, h/4 ... so the leading error term cancels at every
    level.

    Each column of the table removes one more term of the error expansion, so a
    second-order formula becomes fourth order in one column and sixth in the next. The
    gain is real and it is finite: once the round-off floor is reached, another column
    adds nothing.

    GAP IS NOT DECORATION. The centred difference's error contains only EVEN powers of
    h, so its terms are two apart and gap is 2. A one-sided difference has every power,
    so its terms are one apart and gap must be 1. Using the wrong gap divides by the
    wrong number and the column stops cancelling anything -- quietly, because the table
    still fills in."""
    T = np.zeros((levels, levels))
    for i in range(levels):
        T[i, 0] = estimate(x, h / 2.0 ** i)
        for j in range(1, i + 1):
            factor = 2.0 ** (order + gap * (j - 1))
            T[i, j] = T[i, j - 1] + (T[i, j - 1] - T[i - 1, j - 1]) / (factor - 1.0)
    return T
# --8<--


def five_point(f, x, h):
    """A fourth-order first derivative from four values around x.

    Two more evaluations buy two more orders. It is the standard formula wherever the
    function is cheap and the accuracy matters more than the count of calls."""
    return (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12.0 * h)


def gradient(f, x, h=None):
    """The vector of partial derivatives, each by a centred difference.

    Day 6 built this by hand for one Jacobian. It is here so the later days can ask for
    a gradient without rebuilding it, and so the step is chosen by the same rule every
    time."""
    x = np.asarray(x, dtype=float)
    if h is None:
        h = best_step(2)
    g = np.zeros(x.size)
    for i in range(x.size):
        step = np.zeros(x.size)
        step[i] = h
        g[i] = (f(x + step) - f(x - step)) / (2.0 * h)
    return g

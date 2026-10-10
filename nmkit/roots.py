"""Finding a value at which a function is zero. Days 2 and 3.

Day 2 adds the bracketing methods, which cannot fail once a sign change is in hand. Day
3 adds the open methods, which are faster and carry no such guarantee.

Every routine here returns a Result, so a caller can ask what happened rather than only
what the answer was. A root finder that returns a bare float cannot tell a converged run
from an exhausted one, and the difference matters more than the digits."""
import math


class Result:
    """What a root finder returns: the answer, and the record of how it got there.

    `history` holds one entry per iteration. It exists so a chapter can print a table of
    errors and measure the order of convergence, rather than assert one.
    """

    def __init__(self, root, iterations, converged, history=None, why=""):
        self.root = root
        self.iterations = iterations
        self.converged = converged
        self.history = history or []
        self.why = why

    def __repr__(self):
        state = "converged" if self.converged else "STOPPED"
        return (f"Result(root={self.root!r}, iterations={self.iterations}, "
                f"{state}{', ' + self.why if self.why else ''})")


# --8<-- bracket_scan
def bracket_scan(f, a, b, n=50):
    """Walk [a, b] in n steps and return every subinterval whose ends differ in sign.

    A root finder needs a bracket before it can start, and finding one is a separate
    problem from refining it. This scan is deliberately crude: it can only find sign
    changes it steps over, so a root pair closer together than the step is missed. That
    limitation is the reason the chapter shows it failing as well as working."""
    out = []
    h = (b - a) / n
    x0, f0 = a, f(a)
    for i in range(1, n + 1):
        x1 = a + i * h
        f1 = f(x1)
        if f0 == 0.0:
            out.append((x0, x0))
        elif f0 * f1 < 0.0:
            out.append((x0, x1))
        x0, f0 = x1, f1
    return out
# --8<--


# --8<-- bisect
def bisect(f, a, b, tol=1e-12, max_iter=200):
    """Halve a bracket until it is narrower than tol.

    The sign change is checked once, at the start, and then maintained as an invariant:
    after every step one end is still negative and the other still positive. That
    invariant is the whole guarantee, and it is why bisection cannot diverge.

    The midpoint is computed as a + (b - a) / 2 rather than (a + b) / 2. The two agree
    in exact arithmetic. The second can overflow for large ends, and can land outside
    [a, b]."""
    fa, fb = f(a), f(b)
    if fa == 0.0:
        return Result(a, 0, True, [(a, fa)], "the left end was already a root")
    if fb == 0.0:
        return Result(b, 0, True, [(b, fb)], "the right end was already a root")
    if fa * fb > 0.0:
        raise ValueError("f(a) and f(b) have the same sign: this is not a bracket")

    history = []
    for k in range(1, max_iter + 1):
        m = a + (b - a) / 2
        fm = f(m)
        history.append((m, fm))
        if fm == 0.0 or (b - a) / 2 < tol:
            return Result(m, k, True, history)
        if fa * fm < 0.0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return Result(a + (b - a) / 2, max_iter, False, history, "ran out of iterations")
# --8<--


# --8<-- steps_needed
def steps_needed(a, b, tol):
    """How many bisection steps are needed to reach tol, known before the run starts.

    The width after k steps is (b - a) / 2 ** k. Setting that below tol and taking
    base-two logarithms gives the count. Bisection is the only method in this book whose
    cost can be stated in advance, and that is what a guarantee buys."""
    return math.ceil(math.log2((b - a) / tol))
# --8<--


# --8<-- false_position
def false_position(f, a, b, tol=1e-12, max_iter=200, illinois=False):
    """Replace the midpoint with the point where the chord through the ends crosses
    zero.

    The chord uses the function's values, not only the signs, so a nearly straight
    function is solved in a few steps. The cost is that the bracket need not shrink: on
    a convex function one end can stay fixed for every iteration, and the interval never
    approaches zero width.

    `illinois=True` halves the retained end's value whenever the same end is kept twice.
    That one line breaks the stall, and the chapter measures both."""
    fa, fb = f(a), f(b)
    if fa * fb > 0.0:
        raise ValueError("f(a) and f(b) have the same sign: this is not a bracket")

    history = []
    side = 0
    prev = None
    for k in range(1, max_iter + 1):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        history.append((c, fc))
        if fc == 0.0 or (prev is not None and abs(c - prev) < tol):
            return Result(c, k, True, history)
        prev = c
        if fa * fc < 0.0:
            b, fb = c, fc
            if illinois and side == -1:
                fa *= 0.5
            side = -1
        else:
            a, fa = c, fc
            if illinois and side == 1:
                fb *= 0.5
            side = 1
    return Result(prev, max_iter, False, history, "ran out of iterations")
# --8<--


def width_history(f, a, b, steps):
    """The bracket width after each bisection step, for the error tables of Day 2."""
    fa = f(a)
    out = []
    for _ in range(steps):
        m = a + (b - a) / 2
        fm = f(m)
        if fa * fm < 0.0:
            b = m
        else:
            a, fa = m, fm
        out.append(b - a)
    return out


# --------------------------------------------------------------------------------------
# Day 3 — the open methods. No bracket, no guarantee, and far fewer steps when
# they work.
# --------------------------------------------------------------------------------------


# --8<-- fixed_point
def fixed_point(g, x0, tol=1e-12, max_iter=200):
    """Iterate x <- g(x) from x0 until two successive values agree to tol.

    Every root problem can be written this way, and the rearrangement chosen decides
    whether the iteration converges at all. The test is the size of g' near the root:
    below one it contracts, above one it repels, and the routine cannot tell which until
    it has run."""
    history = []
    x = float(x0)
    for k in range(1, max_iter + 1):
        try:
            nxt = g(x)
        except (OverflowError, ValueError) as exc:
            return Result(x, k, False, history, f"g(x) failed: {type(exc).__name__}")
        history.append((nxt, nxt - x))
        if not math.isfinite(nxt):
            return Result(x, k, False, history, "the iteration left the finite numbers")
        if abs(nxt - x) < tol:
            return Result(nxt, k, True, history)
        x = nxt
    return Result(x, max_iter, False, history, "ran out of iterations")
# --8<--


# --8<-- newton
def newton(f, df, x0, tol=1e-12, max_iter=100):
    """Follow the tangent at x to where it meets the axis, and repeat.

    The step is f(x) / f'(x). Two things can go wrong and both are shown in Day 3: the
    derivative can be zero, which makes the step infinite, and the tangent can point
    away from the root, which sends the iteration off to somewhere unrelated. Neither is
    detectable in advance, which is exactly what the bracketing guarantee bought and
    this method sells."""
    history = []
    x = float(x0)
    for k in range(1, max_iter + 1):
        fx = f(x)
        d = df(x)
        if d == 0.0:
            return Result(x, k, False, history, "the derivative is zero: "
                                                "the tangent is flat")
        step = fx / d
        x = x - step
        history.append((x, step))
        if not math.isfinite(x):
            return Result(x, k, False, history, "the iteration left the finite numbers")
        if abs(step) < tol:
            return Result(x, k, True, history)
    return Result(x, max_iter, False, history, "ran out of iterations")
# --8<--


# --8<-- secant
def secant(f, x0, x1, tol=1e-12, max_iter=100):
    """Newton's method with the derivative replaced by a difference of two recent
    points.

    No derivative is needed, which is the whole reason to prefer it: for a function that
    is only available as a program, an exact derivative may not exist in any usable
    form. The price is order 1.618 rather than 2, measured in Example 3.12."""
    history = []
    a, b = float(x0), float(x1)
    fa, fb = f(a), f(b)
    for k in range(1, max_iter + 1):
        if fb == fa:
            return Result(b, k, False, history, "the two points give the same value")
        step = fb * (b - a) / (fb - fa)
        a, fa = b, fb
        b = b - step
        fb = f(b)
        history.append((b, step))
        if not math.isfinite(b):
            return Result(b, k, False, history, "the iteration left the finite numbers")
        if abs(step) < tol:
            return Result(b, k, True, history)
    return Result(b, max_iter, False, history, "ran out of iterations")
# --8<--


# --8<-- newton_modified
def newton_modified(f, df, x0, m, tol=1e-12, max_iter=100):
    """Newton's method with the step multiplied by the multiplicity m of the root.

    At a root of multiplicity m the ordinary step is about 1/m of the distance to the
    root, so the iteration creeps in at first order instead of doubling its digits.
    Multiplying by m restores the full step and with it the second order. The cost is
    that m must be known, and Example 3.20 estimates it from the iteration itself."""
    history = []
    x = float(x0)
    for k in range(1, max_iter + 1):
        d = df(x)
        if d == 0.0:
            return Result(x, k, False, history, "the derivative is zero: "
                                                "the tangent is flat")
        step = m * f(x) / d
        x = x - step
        history.append((x, step))
        if abs(step) < tol:
            return Result(x, k, True, history)
    return Result(x, max_iter, False, history, "ran out of iterations")
# --8<--


# --8<-- order_estimate
def order_estimate(errors):
    """The order of convergence, measured from a sequence of errors rather than assumed.

    If the error obeys e[n+1] = C * e[n] ** p then taking logarithms of two successive
    ratios and dividing removes C and leaves p. Three consecutive errors give one
    estimate, so a run of k errors gives k-2 of them, and a method's order is the value
    they settle on.

    Errors at or below one ulp are dropped first. Once a run has converged its errors
    are rounding noise, and the ratio of two pieces of noise carries no information
    about order -- including it produces a wild final estimate that looks like a real
    measurement."""
    e = [x for x in errors if x > 0.0]
    out = []
    for a, b, c in zip(e, e[1:], e[2:]):
        if b <= 0 or a <= 0 or c <= 0 or a == b or b == c:
            continue
        try:
            out.append(math.log(c / b) / math.log(b / a))
        except (ValueError, ZeroDivisionError):
            continue
    return out
# --8<--

"""The saving is not a constant factor; it grows with every point added."""
import time

import numpy as np

from nmkit.linsolve import solve
from nmkit.spline import thomas


def best_of(fn, inner=20, repeats=5):
    """The shortest of several runs of `inner` calls, divided back down to one call.

    Two separate problems, and both have to be dealt with. A single reading measures
    whatever else the machine was doing, so the shortest of several is taken. And one
    Thomas pass on a small system takes less time than the clock can resolve, so the
    reading of a single call is mostly quantisation -- timing twenty calls together and
    dividing puts the measurement back above the clock's step.
    """
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        for _ in range(inner):
            fn()
        best = min(best, (time.perf_counter() - t0) / inner)
    return best


# Both routines are from this book, so the comparison is between the two ALGORITHMS.
# Timing thomas against a library solver would compare a Python loop with compiled
# LAPACK, which is a fact about the two implementations and not about the count of
# operations either performs.
print(f"{'size':>7} {'Thomas':>11} {'full solve':>12} {'ratio':>9}")
sizes = (100, 200, 400, 800)
ts, fs = [], []
for n in sizes:
    lower = np.full(n - 1, 1.0)
    diag = np.full(n, 4.0)
    upper = np.full(n - 1, 1.0)
    rhs = np.ones(n)
    A = np.diag(diag) + np.diag(lower, -1) + np.diag(upper, 1)
    a = best_of(lambda: thomas(lower, diag, upper, rhs))
    b = best_of(lambda: solve(A, rhs), inner=1, repeats=3)
    ts.append(a)
    fs.append(b)
    print(f"{n:>7} {a:>11.5f} {b:>12.5f} {b / a:>9.2f}")
print()
p_t = np.log2(ts[-1] / ts[0]) / np.log2(sizes[-1] / sizes[0])
p_f = np.log2(fs[-1] / fs[0]) / np.log2(sizes[-1] / sizes[0])
print(f"Thomas grows like n to the power     {p_t:.2f}")
print(f"the full solve like n to the power    {p_f:.2f}")
print("the first is 1 and the second is above "
      "2, so the gap widens with every knot added")

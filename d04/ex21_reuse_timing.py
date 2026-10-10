"""Factoring once and reusing it is the whole reason a factorisation is a separate
object."""
import time

import numpy as np

from nmkit.linsolve import lu_pivot, lu_solve, solve


def best_of(fn, repeats=5):
    """The shortest of several runs, which is the only reproducible one.

    One wall-clock reading of a short operation measures whatever else the machine was
    doing as well. Across two runs of this book's full harness a single reading of this
    comparison moved from 19.7 to 13.2; the shortest of five moves by a few percent.
    """
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        best = min(best, time.perf_counter() - t0)
    return best


rng = np.random.default_rng(29)
n, k = 120, 40
A = rng.uniform(-2, 2, (n, n))
rhs = [rng.uniform(-2, 2, n) for _ in range(k)]


def every_time():
    for b in rhs:
        solve(A, b)


def once():
    LU, piv, _ = lu_pivot(A)
    for b in rhs:
        lu_solve(LU, piv, b)


a, c = best_of(every_time), best_of(once)
print(f"{k} right-hand sides, matrix {n} by {n}")
print(f"  factoring every time : {a:.3f} s")
print(f"  factoring once       : {c:.3f} s")
print(f"  ratio                : {a / c:.1f}")
print()
print(f"the factorisation is done {k} times instead of once, and that is the whole of "
      f"it")

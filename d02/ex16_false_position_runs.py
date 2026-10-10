"""On a nearly straight function the chord converges in a handful of steps."""
import math

from nmkit.roots import bisect, false_position

def f(x):
    return math.exp(x) - 3.0

fp = false_position(f, 0.0, 2.0, tol=1e-14)
bi = bisect(f, 0.0, 2.0, tol=1e-14)
print("true root, log(3) :", f"{math.log(3.0):.15f}")
print("false position    :", f"{fp.root:.15f}", "in", fp.iterations, "steps")
print("bisection         :", f"{bi.root:.15f}", "in", bi.iterations, "steps")

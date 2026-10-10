"""Problem 3.40: a secant run that detects its own failure instead of returning a wrong
answer."""
import math

from nmkit.roots import secant

for name, f, x0, x1 in (
        ("cos(x)-x    ", lambda x: math.cos(x) - x, 0.0, 1.0),
        ("atan(x) far ", math.atan, 5.0, 6.0),
        ("x**2+1 (none)", lambda x: x * x + 1.0, 0.0, 1.0)):
    r = secant(f, x0, x1, tol=1e-13, max_iter=60)
    if r.converged and abs(f(r.root)) < 1e-8:
        print(f"{name}: root {r.root:+.13f}")
    elif r.converged:
        print(f"{name}: STOPPED at {r.root:+.6e} but f there is {f(r.root):+.3e}")
    else:
        print(f"{name}: did not converge -- {r.why}")

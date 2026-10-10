"""Problem 2.36: scan for every bracket in an interval, then refine each one."""
import math

from nmkit.roots import bracket_scan, bisect

def f(x):
    return math.cos(x) - 0.1 * x

for a, b in bracket_scan(f, 0.0, 20.0, n=200):
    r = bisect(f, a, b, tol=1e-14)
    print(f"bracket [{a:6.3f}, {b:6.3f}] -> root {r.root:.13f}  "
          f"f {f(r.root):+.2e}  {r.iterations} steps")

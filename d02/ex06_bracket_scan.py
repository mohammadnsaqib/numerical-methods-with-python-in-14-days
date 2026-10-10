"""Finding a bracket is a different problem from refining one, and it is solved by a
scan."""
import math

from nmkit.roots import bracket_scan, bisect

def f(x):
    return math.sin(x) - 0.3 * x

brackets = bracket_scan(f, -8.0, 8.0, n=60)
print("brackets found:", len(brackets))
for a, b in brackets:
    r = bisect(f, a, b, tol=1e-13)
    print(f"  [{a:+.4f}, {b:+.4f}] -> root {r.root:+.12f}  in {r.iterations} steps")

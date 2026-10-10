"""First order means the digit count grows by a fixed amount per step, not by doubling.
"""
import math

from nmkit.roots import fixed_point

root = 2.0945514815423265
r = fixed_point(lambda x: (2 * x + 5) ** (1 / 3), 2.0, tol=1e-15, max_iter=80)

print(f"{'step':>5} {'correct digits':>16} {'gain':>8}")
prev = None
for k, (x, _) in enumerate(r.history[:12], 1):
    e = abs(x - root)
    d = -math.log10(e / abs(root)) if e > 0 else 16.0
    gain = f"{d - prev:.3f}" if prev is not None else "    --"
    print(f"{k:>5} {d:>16.3f} {gain:>8}")
    prev = d

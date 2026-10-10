"""Two formulas, one step each, and the gap between them at five steps."""
import numpy as np

from nmkit.diff import central_diff, forward_diff

x = 1.0
true = np.cos(x)
print(f"{'h':>8} {'forward error':>16} {'centred error':>16} {'how many times':>16}")
for h in (0.1, 0.01, 0.001, 0.0001, 0.00001):
    ef = abs(forward_diff(np.sin, x, h) - true)
    ec = abs(central_diff(np.sin, x, h) - true)
    print(f"{h:>8.0e} {ef:>16.3e} {ec:>16.3e} {ef / ec:>16.1f}")

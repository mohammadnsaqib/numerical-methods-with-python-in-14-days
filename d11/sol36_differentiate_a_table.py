"""Problem 11.36: derivatives from a table of measurements, with the ends handled
separately."""
import numpy as np

from nmkit.diff import backward_diff, central_diff, forward_diff

# Position of a falling body, sampled every tenth of a second. The true velocity is 9.81
# t.
ts = np.round(np.arange(0.0, 1.01, 0.1), 10)
xs = 0.5 * 9.81 * ts ** 2
h = 0.1

print(f"{'t':>5} {'formula':>10} {'velocity':>11} {'exact':>9} {'error':>10}")
for i, t in enumerate(ts):
    if i == 0:
        v, name = (xs[1] - xs[0]) / h, "forward"
    elif i == ts.size - 1:
        v, name = (xs[-1] - xs[-2]) / h, "backward"
    else:
        v, name = (xs[i + 1] - xs[i - 1]) / (2 * h), "centred"
    print(f"{t:>5.1f} {name:>10} {v:>11.6f} {9.81 * t:>9.4f} "
          f"{abs(v - 9.81 * t):>10.3e}")
print()
print("the interior is exact for a parabola, and only the two ends carry an error")

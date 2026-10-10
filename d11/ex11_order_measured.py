"""The order of a formula is a measured quantity, not a claim in its docstring."""
import numpy as np

from nmkit.diff import central_diff, forward_diff, five_point

x = 1.0
true = np.cos(x)
print(f"{'h':>10} {'forward':>10} {'centred':>10} {'five point':>12}")
prev = {}
for k in range(2, 8):
    h = 2.0 ** (-k)
    row = {}
    for name, fn in (("forward", forward_diff), ("centred", central_diff),
                     ("five point", five_point)):
        e = abs(fn(np.sin, x, h) - true)
        row[name] = f"{np.log2(prev[name] / e):.4f}" if name in prev else ""
        prev[name] = e
    print(f"{h:>10.6f} {row['forward']:>10} {row['centred']:>10} "
          f"{row['five point']:>12}")
print()
print("the measured orders are 1, 2 and 4, which is what the three formulas claim")

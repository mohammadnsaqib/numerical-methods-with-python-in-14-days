"""Problem 2.37: the predicted step count against the measured one, over six tolerances.
"""
import math

from nmkit.roots import bisect, steps_needed

a, b = 0.0, 3.0
print(f"{'tolerance':>12} {'predicted':>10} {'actual':>8} {'agree':>7}")
for p in range(2, 14, 2):
    tol = 10.0 ** -p
    pred = steps_needed(a, b, tol)
    act = bisect(math.cos, a, b, tol=tol).iterations
    print(f"{tol:>12.0e} {pred:>10} {act:>8} {str(pred == act):>7}")

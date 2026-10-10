"""Problem 2.38: the bracket after each step, printed with the width it guarantees."""
from nmkit.roots import width_history

def f(x):
    return x ** 2 - 2.0

widths = width_history(f, 1.0, 2.0, 12)
print(f"{'step':>5} {'width':>14} {'ratio to previous':>19}")
prev = None
for k, w in enumerate(widths, 1):
    ratio = f"{w / prev:.6f}" if prev else "     --"
    print(f"{k:>5} {w:>14.10f} {ratio:>19}")
    prev = w

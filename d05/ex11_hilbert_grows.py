"""The Hilbert matrix's conditioning grows so fast that size 13 is past double
precision."""
import numpy as np

from nmkit.norms import cond, digits_lost, hilbert

print(f"{'n':>4} {'condition number':>18} {'digits lost':>13} "
      f"{'digits left of 16':>19}")
for n in range(2, 14):
    A = hilbert(n)
    k, d = cond(A, 2), digits_lost(A, 2)
    print(f"{n:>4} {k:>18.4e} {d:>13.2f} {max(0.0, 16 - d):>19.2f}")

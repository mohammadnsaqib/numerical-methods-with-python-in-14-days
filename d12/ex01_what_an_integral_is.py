"""The integral as the limit of a sum of rectangles, computed at six counts."""
import numpy as np
from mpmath import mp, quad as mpquad, sin as mpsin

mp.dps = 40
exact = float(mpquad(mpsin, [0, mp.pi]))

print(f"{'rectangles':>12} {'their total area':>20} {'error':>12}")
for n in (4, 16, 64, 256, 1024, 4096):
    x = np.linspace(0.0, np.pi, n + 1)
    total = float(np.sum(np.sin(x[:-1]) * (np.pi / n)))
    print(f"{n:>12} {total:>20.14f} {abs(total - exact):>12.3e}")
print(f"{'exact':>12} {exact:>20.14f}")

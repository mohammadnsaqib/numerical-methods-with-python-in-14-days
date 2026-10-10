"""Two second-order estimates combined into one fourth-order estimate."""
import numpy as np

from nmkit.diff import central_diff

x, h = 1.0, 0.2
true = np.cos(x)
a = central_diff(np.sin, x, h)
b = central_diff(np.sin, x, h / 2)

# The error of the centred difference is C h^2 plus smaller terms. Halving the step
# divides that term by 4, so (b - a) / 3 estimates it, and adding that estimate to b
# removes it.
r = b + (b - a) / 3.0
print(f"estimate at h = {h}       : {a:.15f}   error {abs(a - true):.3e}")
print(f"estimate at h = {h / 2}      : {b:.15f}   error {abs(b - true):.3e}")
print(f"the correction (b - a) / 3 : {(b - a) / 3.0:+.15f}")
print(f"combined                   : {r:.15f}   error {abs(r - true):.3e}")
print()
print(f"the combination is better than the better of the two by "
      f"{abs(b - true) / abs(r - true):.0f} times")

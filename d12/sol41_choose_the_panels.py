"""Problem 12.41: where the adaptive rule actually put its panels."""
import numpy as np

from nmkit.quad import simpson


def peak(t):
    """The same spike as Example 12.21, of width about 0.001 at 0.3."""
    return 1.0 / (1.0 + 1e6 * (t - 0.3) ** 2)


panels = []


def step(lo, hi, whole, k, tol):
    """Adaptive Simpson, recording every panel it decides not to split again."""
    mid = (lo + hi) / 2.0
    left, right = simpson(peak, lo, mid), simpson(peak, mid, hi)
    if k <= 0 or abs(left + right - whole) <= 15.0 * tol:
        panels.append((lo, hi))
        return left + right + (left + right - whole) / 15.0
    return step(lo, mid, left, k - 1, tol) + step(mid, hi, right, k - 1, tol)


step(0.0, 1.0, simpson(peak, 0.0, 1.0), 50, 1e-10)
panels.sort()
widths = np.array([hi - lo for lo, hi in panels])
print(f"panels used            : {len(panels)}")
print(f"widest panel           : {widths.max():.6f}")
print(f"narrowest panel        : {widths.min():.3e}")
print(f"ratio                  : {widths.max() / widths.min():.0f}")
print()
print(f"{'region':>22} {'panels':>8} {'share of the width':>20}")
for lo, hi, name in ((0.0, 0.29, "left of the peak"), (0.29, 0.31, "at the peak"),
                     (0.31, 1.0, "right of the peak")):
    inside = [p for p in panels if p[0] >= lo - 1e-12 and p[1] <= hi + 1e-12]
    print(f"{name:>22} {len(inside):>8} {(hi - lo) * 100:>19.1f}%")

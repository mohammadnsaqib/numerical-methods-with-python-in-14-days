"""The two errors together: a curve that falls, turns and rises."""
import numpy as np

from nmkit.diff import central_diff

x = 1.0
true = np.cos(x)
hs = 10.0 ** np.arange(-1.0, -16.5, -0.5)
errs = np.array([abs(central_diff(np.sin, x, h) - true) for h in hs])
best = int(np.argmin(errs))
print(f"{'h':>10} {'error':>12}")
for h, e in zip(hs[::2], errs[::2]):
    print(f"{h:>10.2e} {e:>12.3e}")
print()
print(f"the smallest error is {errs[best]:.3e} at h = {hs[best]:.2e}")
print(f"at h = {hs[-1]:.0e} the error is {errs[-1]:.3e}, which is worse by "
      f"{errs[-1] / errs[best]:.0f} times")

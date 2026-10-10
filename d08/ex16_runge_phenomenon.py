"""On another function, equally spaced, more points make the answer worse."""
import numpy as np

from nmkit.interp import lagrange_eval, runge

t = np.linspace(-1.0, 1.0, 1000)
print(f"{'points':>8} {'largest error':>16}")
for n in (5, 9, 13, 17, 21):
    xs = np.linspace(-1.0, 1.0, n)
    e = np.max(np.abs(runge(t) - lagrange_eval(xs, runge(xs), t)))
    print(f"{n:>8} {e:>16.4e}")

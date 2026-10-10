"""On a well-behaved function more points always help, and the improvement is quick."""
import numpy as np

from nmkit.interp import lagrange_eval

f = np.exp
t = np.linspace(0.0, 1.0, 500)
print(f"{'points':>8} {'largest error':>16} {'ratio':>10}")
prev = None
for n in (3, 4, 5, 6, 7, 8):
    xs = np.linspace(0.0, 1.0, n)
    e = np.max(np.abs(f(t) - lagrange_eval(xs, f(xs), t)))
    ratio = f"{e / prev:.5f}" if prev else "    --"
    print(f"{n:>8} {e:>16.3e} {ratio:>10}")
    prev = e

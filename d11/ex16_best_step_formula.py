"""The step that balances the two errors, computed before anything is run."""
import numpy as np

from nmkit.diff import best_step, central_diff, forward_diff

eps = np.finfo(float).eps
print(f"the machine epsilon is {eps:.6e}")
print(f"forward difference: h ~ sqrt(eps)      = {best_step(1):.6e}")
print(f"centred difference: h ~ cube root(eps) = {best_step(2):.6e}")
print()
x = 1.0
true = np.cos(x)
hs = 10.0 ** np.arange(-2.0, -12.01, -0.1)
for name, fn, order in (("forward", forward_diff, 1), ("centred", central_diff, 2)):
    errs = np.array([abs(fn(np.sin, x, h) - true) for h in hs])
    found = hs[int(np.argmin(errs))]
    print(f"{name:>8}: predicted {best_step(order):.3e}, measured {found:.3e}, "
          f"error there {errs.min():.3e}")

"""Problem 13.39: what step control is worth, and the feature it can step straight over.
"""
import numpy as np

from nmkit.ode import adaptive_rk, rk4


def f(t, y):
    """A decay driven by a pulse a hundredth of a unit wide, in an interval of six."""
    return -y + 10.0 * np.exp(-40000.0 * (t - 3.0) ** 2)


ref_ts, ref_ys, _, _ = adaptive_rk(f, 0.0, 1.0, 6.0, tol=1e-13, h0=1e-3)
exact_end = float(ref_ys[-1])
print(f"the reference value at t = 6 is {exact_end:.15f}")
print()
print(f"{'method':>30} {'calls':>8} {'error':>13}")
for n in (200, 800, 3200):
    e = abs(float(rk4(f, 0.0, 1.0, 6.0 / n, n)[1][-1]) - exact_end)
    print(f"{'RK4, ' + str(n) + ' fixed steps':>30} {4 * n:>8} {e:>13.3e}")
print()

# The controller only ever measures the error of the step it just took. A first step
# wider than the pulse lands on the far side of it, both estimates agree that nothing
# happened, and the step is accepted. Nothing in the method reports a failure.
for tol in (1e-6, 1e-8, 1e-10):
    ts, ys, ok, bad = adaptive_rk(f, 0.0, 1.0, 6.0, tol=tol)
    print(f"{'adaptive, first step 0.06, tol ' + f'{tol:.0e}':>30} {6 * (ok + bad):>8} "
          f"{abs(float(ys[-1]) - exact_end):>13.3e}")
print()
for tol in (1e-6, 1e-8, 1e-10):
    ts, ys, ok, bad = adaptive_rk(f, 0.0, 1.0, 6.0, tol=tol, h0=1e-3)
    print(f"{'adaptive, first '
             'step 0.001, tol ' + f'{tol:.0e}':>30} {6 * (ok + bad):>8} "
          f"{abs(float(ys[-1]) - exact_end):>13.3e}")
print()
print("At tol 1e-10 the adaptive rule beats 3200 fixed steps by six decades on a third")
print("of the evaluations. At tol 1e-6 it misses the pulse entirely and reports no")
print("trouble, and a smaller first step does "
      "not save it: the controller is allowed to")
print("grow the step fivefold per success, so by t = 3 it is wide again. An error")
print("estimate is a statement about the step that WAS taken, never about what was")
print("skipped over.")

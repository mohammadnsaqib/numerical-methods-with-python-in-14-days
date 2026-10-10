"""Problem 3.41: estimate the multiplicity from the run, then use it, without being
told."""
from nmkit.roots import newton, newton_modified

def solve_auto(f, df, x0, tol=1e-13):
    """Run plain Newton a little way, read the multiplicity off the error ratio, then
    finish.

    The ratio of successive steps settles on 1 - 1/m, so m is 1/(1 - ratio). It is
    rounded to the nearest whole number, because a multiplicity is a count and a
    fractional one means the estimate has not settled yet.
    """
    probe = newton(f, df, x0, tol=1e-8, max_iter=40)
    steps = [s for _, s in probe.history if s != 0.0]
    if len(steps) < 3:
        return probe.root, 1, probe.iterations
    ratio = steps[-1] / steps[-2]
    m = max(1, round(1.0 / (1.0 - ratio))) if ratio < 0.999 else 1
    final = newton_modified(f, df, probe.root, m=m, tol=tol, max_iter=40)
    return final.root, m, probe.iterations + final.iterations

cases = [
    ("simple root  ", lambda x: x * x - 2.0, lambda x: 2 * x, 1.0, 1.4142135623730951),
    ("double root  ", lambda x: (x - 1.0) ** 2 * (x - 3.0),
     lambda x: 2 * (x - 1.0) * (x - 3.0) + (x - 1.0) ** 2, 1.6, 1.0),
    ("triple root  ", lambda x: (x - 1.0) ** 3 * (x - 3.0),
     lambda x: 3 * (x - 1.0) ** 2 * (x - 3.0) + (x - 1.0) ** 3, 1.6, 1.0),
]
for name, f, df, x0, want in cases:
    root, m, steps = solve_auto(f, df, x0)
    print(f"{name}: m estimated as {m}, root {root:.14f}, error "
          f"{abs(root - want):.2e}, {steps} steps in all")

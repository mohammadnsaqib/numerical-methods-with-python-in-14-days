"""Problem 2.41: a stopping rule scaled to the size of the root, so it works at any
magnitude."""
def bisect_rel(f, a, b, rtol=1e-12, max_iter=200):
    """Bisect until the bracket is narrow RELATIVE to where the root sits."""
    fa = f(a)
    for k in range(1, max_iter + 1):
        m = a + (b - a) / 2
        fm = f(m)
        # The absolute floor keeps the rule usable when the root is at or near zero,
        # where a purely relative test can never be satisfied.
        if fm == 0.0 or (b - a) / 2 < rtol * max(abs(m), 1e-300) + 1e-300:
            return m, k
        if fa * fm < 0.0:
            b = m
        else:
            a, fa = m, fm
    return a + (b - a) / 2, max_iter

for target, lo, hi in ((1e-8, -1.0, 1.0), (1.0, 0.0, 3.0), (1e8, 0.0, 1e9)):
    root, steps = bisect_rel(lambda x: x - target, lo, hi)
    print(f"root near {target:<8.0e} found {root:.13e} in {steps:>3} steps, "
          f"relative error {abs(root - target) / target:.2e}")

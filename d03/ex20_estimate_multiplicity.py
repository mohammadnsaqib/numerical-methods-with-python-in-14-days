"""The multiplicity does not have to be known in advance: the error ratio reveals it."""
from nmkit.roots import newton

for m, f, df in (
    (2, lambda x: (x - 1.0) ** 2 * (x - 3.0),
     lambda x: 2 * (x - 1.0) * (x - 3.0) + (x - 1.0) ** 2),
    (3, lambda x: (x - 1.0) ** 3 * (x - 3.0),
     lambda x: 3 * (x - 1.0) ** 2 * (x - 3.0) + (x - 1.0) ** 3),
):
    r = newton(f, df, 1.6, tol=1e-13, max_iter=80)
    errs = [abs(x - 1.0) for x, _ in r.history if abs(x - 1.0) > 1e-9]
    ratio = errs[-1] / errs[-2]
    print(f"true multiplicity {m}: error ratio {ratio:.6f}, "
          f"so m is about {1 / (1 - ratio):.3f}")

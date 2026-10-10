"""Through any n points with distinct x there is exactly one polynomial of degree below
n."""
import numpy as np

xs = np.array([0.0, 1.0, 2.0])
ys = np.array([1.0, 3.0, 2.0])

for c in ([1.0, 3.0, -1.5], [1.0, 3.5, -1.5], [0.0, 0.0, 0.0]):
    p = np.polynomial.Polynomial(c)
    hits = [f"{p(x):.4f}" for x in xs]
    print(f"coefficients {c}: values at the nodes {hits}   passes: "
          f"{np.allclose(p(xs), ys)}")

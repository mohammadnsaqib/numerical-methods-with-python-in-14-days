"""The nodes that make the largest value of that product as small as it can be."""
import numpy as np

from nmkit.interp import chebyshev_nodes

for n in (5, 9):
    even = np.linspace(-1.0, 1.0, n)
    cheb = chebyshev_nodes(-1.0, 1.0, n)
    print(f"{n} points")
    print("  equally spaced:", np.array2string(even, precision=4))
    print("  Chebyshev     :", np.array2string(cheb, precision=4))
    print("  gap at the end:", f"{even[1] - even[0]:.4f}", "against",
          f"{cheb[1] - cheb[0]:.4f}")

"""The nodes are not on a grid, and that is the whole idea."""
import numpy as np

for n in (2, 3, 4, 5):
    x, w = np.polynomial.legendre.leggauss(n)
    print(f"n = {n}")
    print("  nodes  : " + " ".join(f"{v:>10.6f}" for v in x))
    print("  weights: " + " ".join(f"{v:>10.6f}" for v in w))
print()
print(f"the weights always add to 2, the width of [-1, 1]: "
      f"{np.sum(np.polynomial.legendre.leggauss(5)[1]):.15f}")
print("no node ever sits at an endpoint, so an integrand may be undefined there")

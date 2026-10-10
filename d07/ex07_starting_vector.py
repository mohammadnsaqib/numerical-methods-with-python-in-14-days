"""A start with no component along the dominant direction cannot find it, in exact
arithmetic."""
import numpy as np

from nmkit.eigen import power_method

A = np.array([[3.0, 1.0], [1.0, 3.0]])
e2 = np.array([1.0, -1.0]) / np.sqrt(2)              # exactly the OTHER eigenvector

lam, v, k, _ = power_method(A, x0=e2, tol=1e-13, max_iter=200)
print("started exactly on the second eigenvector")
print("eigenvalue found:", f"{lam:.13f}", " after", k, "iterations")
print("the largest eigenvalue is 4.0")
print("\nrounding never introduced a component along e1, so the method stayed where it "
      "began.")

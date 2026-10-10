"""Addition is not associative in floating point, so the order of a sum changes its
value."""
import numpy as np

terms = np.array([1.0 / n ** 2 for n in range(1, 1_000_001)])

ascending = 0.0
for t in terms:
    ascending += t

descending = 0.0
for t in terms[::-1]:
    descending += t

print("largest first :", f"{ascending:.17g}")
print("smallest first:", f"{descending:.17g}")
print("they differ   :", ascending != descending)
print("difference    :", f"{abs(ascending - descending):.3e}")

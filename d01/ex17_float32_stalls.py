"""In a narrow format a running total stops growing while the terms are still positive.
"""
import numpy as np

total = np.float32(0.0)
one = np.float32(1.0)
n = 0
while True:
    n += 1
    term = one / np.float32(n)
    new = np.float32(total + term)
    if new == total:
        break
    total = new

print("the float32 harmonic sum stopped at n =", n)
print("running total :", total)
print("the term added:", np.float32(1.0) / np.float32(n))
print("but the true harmonic series has no finite sum.")

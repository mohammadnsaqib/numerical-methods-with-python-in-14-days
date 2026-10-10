"""Carrying the lost low-order bits in a second variable recovers most of the accuracy.
"""
from fractions import Fraction

import numpy as np

terms = [1.0 / n ** 2 for n in range(1, 1_000_001)]
# every term added with no round-off at all
exact = float(sum(Fraction(t) for t in terms))

naive = 0.0
for t in terms:
    naive += t

total, comp = 0.0, 0.0
for t in terms:
    y = t - comp
    s = total + y
    comp = (s - total) - y
    total = s

print("exact sum of the stored terms:", f"{exact:.17g}")
print("naive running total          :", f"{naive:.17g}   err {abs(naive - exact):.3e}")
print("compensated running total    :", f"{total:.17g}   err {abs(total - exact):.3e}")

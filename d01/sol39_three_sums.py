"""Problem 1.39: three summation orders measured against a sum that never rounds."""
from fractions import Fraction

terms = [1.0 / n ** 1.5 for n in range(1, 200_001)]
exact = float(sum(Fraction(t) for t in terms))

def naive(seq):
    total = 0.0
    for t in seq:
        total += t
    return total

def compensated(seq):
    total, comp = 0.0, 0.0
    for t in seq:
        y = t - comp
        s = total + y
        comp = (s - total) - y
        total = s
    return total

for name, value in (("largest first ", naive(terms)),
                    ("smallest first", naive(terms[::-1])),
                    ("compensated   ", compensated(terms))):
    print(f"{name}: {value:.17g}   abs err {abs(value - exact):.3e}")

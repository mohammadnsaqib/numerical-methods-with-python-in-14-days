"""Epsilon is a relative gap, so its absolute size grows with the number it is measured
at."""
from nmkit.fp import ulp

EPS = 2.0 ** -52
for x in (1.0, 100.0, 1e6, 1e12):
    gap = ulp(x)
    print(f"x = {x:<8g}  gap = {gap:.4e}   gap / x = {gap / x:.4e}")

print()
print("the ratio is always within a factor of two of epsilon:", f"{EPS:.4e}")

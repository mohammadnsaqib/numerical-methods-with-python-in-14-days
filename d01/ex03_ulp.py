"""The gaps between representable numbers are not equal, so an absolute error means
nothing alone."""
from nmkit.fp import ulp

for x in (1.0, 2.0, 1e3, 1e6, 1e16, 1e300):
    print(f"x = {x:<10g}  gap to the next number = {ulp(x):.6e}")

print()
print("at 1e16 the gap is", ulp(1e16), "so adding 1 changes nothing:")
print("  1e16 + 1 == 1e16 :", 1e16 + 1 == 1e16)

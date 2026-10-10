"""A recurrence that is correct in algebra can still destroy an answer, because it
amplifies its own round-off."""
import math

# I(n) = integral of x**n * e**(x-1) from 0 to 1 obeys I(n) = 1 - n * I(n-1).
I = 1.0 - 1.0 / math.e
print(f"{'n':>4} {'I(n) forward':>22}")
for n in range(1, 19):
    I = 1.0 - n * I
    print(f"{n:>4} {I:>22.15f}")

print("\nevery I(n) must lie between 0 and 1, because the integrand does.")

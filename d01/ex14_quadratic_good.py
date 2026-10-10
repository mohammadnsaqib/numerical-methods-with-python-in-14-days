"""Rationalising the numerator removes the subtraction and returns every digit."""
import math

from mpmath import mp, mpf, sqrt as msqrt

from nmkit.err import rel_err

a, b, c = 1.0, 1e8, 1.0
disc = math.sqrt(b * b - 4 * a * c)
r2 = (-b - disc) / (2 * a)                  # this root never subtracts close numbers
r1 = c / (a * r2)  # and this one comes from the product of the roots

mp.dps = 40
true1 = (-mpf(b) + msqrt(mpf(b) ** 2 - 4 * mpf(a) * mpf(c))) / (2 * mpf(a))
naive = (-b + disc) / (2 * a)  # the formula of the previous example, for comparison

print("oracle root 1 :", str(true1)[:24])
print("naive  root 1 :", f"{naive:.17e}   rel err {rel_err(naive, float(true1)):.3e}")
print("stable root 1 :", f"{r1:.17e}   rel err {rel_err(r1, float(true1)):.3e}")
print("product r1*r2 :", f"{r1 * r2:.17g}", "and c/a is", c / a)

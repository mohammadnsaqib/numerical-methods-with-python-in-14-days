"""Running the same recurrence backwards divides the error instead of multiplying it."""
from mpmath import mp, mpf, quad, exp as mexp

mp.dps = 30
true18 = quad(lambda t: t ** 18 * mexp(t - 1), [0, 1])   # the oracle, computed directly

I = 0.0                       # a deliberately wrong start, far above the true value
for n in range(40, 18, -1):   # backwards: I(n-1) = (1 - I(n)) / n
    I = (1.0 - I) / n

print("started the backward run from a wrong value of 0 at n = 40")
print("backward I(18) :", f"{I:.15f}")
print("oracle   I(18) :", str(true18)[:17])
print("absolute error :", f"{abs(I - float(true18)):.3e}")

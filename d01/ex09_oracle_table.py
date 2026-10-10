"""The error a table reports is only meaningful against a value the book did not compute
in double precision."""
from mpmath import mp, mpf, sqrt as msqrt

from nmkit.err import error_table, print_error_table

mp.dps = 50
true = msqrt(mpf(2))                       # the oracle: fifty correct digits
print("oracle sqrt(2) :", true)

guesses, x = [], 1.0
for _ in range(5):                          # Newton's iteration for sqrt(2), by hand
    x = 0.5 * (x + 2.0 / x)
    guesses.append(x)

print_error_table(error_table(guesses, true, labels=[str(i) for i in range(1, 6)]))

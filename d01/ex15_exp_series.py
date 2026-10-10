"""Summing a series with alternating signs cancels; computing the reciprocal of the
positive one does not."""
import math

def exp_series(x, terms=120):
    term, total = 1.0, 1.0
    for n in range(1, terms):
        term *= x / n
        total += term
    return total

x = -25.0
direct = exp_series(x)
reciprocal = 1.0 / exp_series(-x)
true = math.exp(x)

print("exp(-25) by the series directly :", f"{direct:.6e}")
print("exp(-25) as 1 / exp(+25)        :", f"{reciprocal:.6e}")
print("math.exp(-25)                   :", f"{true:.6e}")
print("relative error, direct     :", f"{abs(direct - true) / true:.3e}")
print("relative error, reciprocal :", f"{abs(reciprocal - true) / true:.3e}")

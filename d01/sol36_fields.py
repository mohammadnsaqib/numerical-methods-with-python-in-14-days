"""Problem 1.36: report the three stored fields of a float, and rebuild it from them."""
from nmkit.fp import decompose, ulp

for x in (1.0, 0.375, -2.5, 1e-7):
    sign, exp, sig = decompose(x)
    rebuilt = sign * sig * 2.0 ** exp
    print(f"x = {x:<10g} sign {sign:>2}  exp {exp:>5}  sig {sig:.15f}")
    print(f"{'':13} ulp {ulp(x):.4e}   rebuilt exactly ? {rebuilt == x}")

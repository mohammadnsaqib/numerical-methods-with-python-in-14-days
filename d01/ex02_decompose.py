"""Every double is a sign, an exponent and a significand, and they can be read back out.
"""
from nmkit.fp import decompose

for x in (1.0, 0.1, 6.5, -3.0, 1e300):
    sign, exp, sig = decompose(x)
    rebuilt = sign * sig * 2.0 ** exp
    print(f"{x:>10g}  sign {sign:>2}  exp {exp:>6}  sig {sig:.17f}  -> {rebuilt:g}")

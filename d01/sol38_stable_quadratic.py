"""Problem 1.38: both roots of a quadratic, computed so that neither is found by
cancellation."""
import math

def roots(a, b, c):
    """Return the two real roots, choosing the sign that avoids a subtraction."""
    d = math.sqrt(b * b - 4 * a * c)
    # Adding two quantities of the SAME sign is what removes the cancellation, so the
    # sign of the square root is chosen to match the sign of b rather than fixed in
    # advance.
    q = -0.5 * (b + math.copysign(d, b))
    return q / a, c / q

for a, b, c in ((1.0, 1e8, 1.0), (1.0, -1e8, 1.0), (1.0, -3.0, 2.0)):
    r1, r2 = roots(a, b, c)
    print(f"a={a:<5g} b={b:<10g} c={c:<5g} -> {r1:.15e}  {r2:.15e}")
    print(f"{'':28} product {r1 * r2:.15g}, c/a is {c / a:g}")

"""What a floating-point number is made of. Day 1.

Nothing here computes an answer. These routines open a stored number up so that the rest
of the book can talk about the gap between a number and its stored form without
hand-waving."""
import math
import struct
from fractions import Fraction

EPS = 2.0 ** -52          # the gap between 1.0 and the next number above it
TINY = 2.0 ** -1022       # the smallest positive normal double
MAXD = (2 - 2.0 ** -52) * 2.0 ** 1023


# --8<-- decompose
def decompose(x):
    """Return (sign, exponent, significand) for a double, as stored.

    The value is sign * significand * 2 ** exponent, with the significand in [1, 2) for
    a normal number. struct is used rather than arithmetic so the answer is the bit
    pattern itself and not a reconstruction of it."""
    bits = struct.unpack(">Q", struct.pack(">d", x))[0]
    sign = -1 if bits >> 63 else 1
    raw_exp = (bits >> 52) & 0x7FF
    frac = bits & ((1 << 52) - 1)
    if raw_exp == 0:                       # subnormal: no implied leading 1
        return sign, -1022, frac / 2.0 ** 52
    return sign, raw_exp - 1023, 1.0 + frac / 2.0 ** 52
# --8<--


# --8<-- ulp
def ulp(x):
    """The unit in the last place at x: the distance to the next representable number.

    This is the resolution of the number line where x sits. It is not a constant; it
    doubles every time the exponent does, which is why an absolute error means nothing
    until the magnitude it belongs to is stated."""
    x = abs(float(x))
    if x == 0.0:
        return 2.0 ** -1074
    return math.nextafter(x, math.inf) - x
# --8<--


def exact(x):
    """The stored value of x as a Fraction: the number the machine actually holds.

    A double is a binary rational, so it has a finite decimal expansion and can be
    written down in full. Printing that expansion is the only way to show that 0.1 is
    not 0.1."""
    return Fraction(x)


def as_decimal(x, digits=25):
    """The stored value of x written out to `digits` significant decimal figures."""
    f = Fraction(x)
    if f == 0:
        return "0"
    sign = "-" if f < 0 else ""
    f = abs(f)
    e = 0
    while f >= 10:
        f /= 10
        e += 1
    while f < 1:
        f *= 10
        e -= 1
    scaled = f * 10 ** (digits - 1)
    n = scaled.numerator // scaled.denominator
    s = str(n)
    return f"{sign}{s[0]}.{s[1:]}e{e:+03d}"


def spacing_table(values):
    """(value, exponent, ulp) for each value, for showing that the gaps are not
    equal."""
    rows = []
    for v in values:
        _, e, _ = decompose(v)
        rows.append((v, e, ulp(v)))
    return rows

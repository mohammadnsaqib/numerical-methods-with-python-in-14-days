"""Problem 3.38: a reciprocal computed by Newton, using no division at all."""
def reciprocal(a, x0=None, steps=6):
    """Solve 1/x - a = 0. The Newton step for it is x <- x * (2 - a * x): only
    multiplies."""
    x = x0 if x0 is not None else 2.0 ** -(a.bit_length() if isinstance(a,
                                           int) else 0) or 0.1
    for _ in range(steps):
        x = x * (2.0 - a * x)
    return x

for a, start in ((3.0, 0.3), (17.0, 0.05), (0.7, 1.2)):
    got = reciprocal(a, start)
    print(f"1/{a:<5} by Newton: {got:.17f}   by division: {1.0 / a:.17f}   "
          f"agree: {got == 1.0 / a}")

"""The cost of bisection is known before it runs, which no other method in this book
allows."""
import math

from nmkit.roots import bisect, steps_needed

cases = [
    ("cos on [0, 3]      ", math.cos, 0.0, 3.0, 1e-6),
    ("cos on [0, 3]      ", math.cos, 0.0, 3.0, 1e-12),
    ("x**3-2x-5 on [2, 3]", lambda x: x ** 3 - 2 * x - 5, 2.0, 3.0, 1e-15),
    ("sin on [2, 4]      ", math.sin, 2.0, 4.0, 1e-9),
]
for name, f, a, b, tol in cases:
    predicted = steps_needed(a, b, tol)
    actual = bisect(f, a, b, tol=tol).iterations
    print(f"{name} tol {tol:<8.0e} predicted {predicted:>3}  actual {actual:>3}")

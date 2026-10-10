"""One table, four methods, three problems: the comparison the chapter has been building
to."""
import math

from nmkit.roots import bisect, false_position, newton, secant

def cell(r):
    """The step count, marked when the run did not actually converge.

    A bare number hides a failure as though it were slowness. The tenth-power row has
    two methods that reach their cap, and without the mark the table would read as
    though they had simply taken longer.
    """
    return f"{r.iterations}" if r.converged else f"{r.iterations}!"

cases = [
    ("x**3-2x-5", lambda x: x ** 3 - 2 * x - 5, lambda x: 3 * x * x - 2, 2.0, 3.0),
    ("cos(x)-x  ", lambda x: math.cos(x) - x, lambda x: -math.sin(x) - 1, 0.0, 1.0),
    ("x**10-1   ", lambda x: x ** 10 - 1, lambda x: 10 * x ** 9, 0.5, 1.3),
]
print(f"{'function':<12}{'bisect':>8}{'false pos':>11}{'secant':>8}{'newton':>8}")
for name, f, df, a, b in cases:
    row = [cell(bisect(f, a, b, tol=1e-13)),
           cell(false_position(f, a, b, tol=1e-13, max_iter=500)),
           cell(secant(f, a, b, tol=1e-13)),
           cell(newton(f, df, b, tol=1e-13))]
    print(f"{name:<12}{row[0]:>8}{row[1]:>11}{row[2]:>8}{row[3]:>8}")
print("\n! marks a run that hit its iteration cap without converging.")

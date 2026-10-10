"""Three integrals: one elementary, one with a name, and one with neither."""
import sympy as sp

t = sp.Symbol("t")
for expr in (t ** 3 * sp.exp(t), sp.exp(-t ** 2), sp.exp(sp.sin(t))):
    result = sp.integrate(expr, t)
    kind = "unevaluated" if result.has(sp.Integral) else "found"
    print(f"integral of {str(expr):>12} : {kind}")
    print(f"{'':>27}{str(result)}")
print()
definite = sp.integrate(sp.exp(sp.sin(t)), (t, 0, 1))
print(f"even the definite form comes back as: {definite}")
print(f"its value has to be computed: {float(definite.evalf()):.15f}")

"""A horizontal tangent never meets the axis, so the step is undefined rather than
large."""
from nmkit.roots import newton

# f'(0) is exactly 0 here, so the guard has something exact to catch.
f = lambda x: x * x - 4.0
df = lambda x: 2.0 * x

print("exactly flat:")
r = newton(f, df, 0.0, tol=1e-13)
print("  ", r)

# And the near-miss, which is the case that actually happens: the derivative is not
# zero, so nothing is caught, and the step is merely enormous.
g = lambda x: x ** 3 - 2 * x - 5
dg = lambda x: 3 * x * x - 2
start = (2.0 / 3.0) ** 0.5
print("\nalmost flat:")
print("   f'(start) =", f"{dg(start):.3e}", " so the first step is",
      f"{-g(start) / dg(start):.3e}")

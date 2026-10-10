"""The same equation can be rearranged into many iterations, and they are not
equivalent."""
import math

# x**3 - 2x - 5 = 0, written three ways as x = g(x).
g1 = lambda x: (2 * x + 5) ** (1 / 3)
g2 = lambda x: (x ** 3 - 5) / 2
g3 = lambda x: 5 / (x * x - 2)

root = 2.0945514815423265
for name, g in (("cube root form", g1), ("solve for the linear term", g2),
                ("solve for the constant", g3)):
    print(f"{name:<26} g(root) = {g(root):.15f}")

print("\nevery one returns the root unchanged, so all three are correct "
      "rearrangements.")

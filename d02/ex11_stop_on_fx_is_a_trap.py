"""Stopping when f(x) is small measures the wrong thing on a function with a flat root.
"""
def flat(x):
    return (x - 1.0) ** 5

def steep(x):
    return 1e6 * (x - 1.0)

for name, f in (("flat  (x-1)**5", flat), ("steep 1e6*(x-1)", steep)):
    x = 1.0 + 1e-2
    print(f"{name}: at x = 1.01, f(x) = {f(x):+.6e}, distance from the root = "
          f"{abs(x - 1):.0e}")

print()
print("a small f value can sit far from the root, and a large one can sit close to it.")

"""A root the curve touches without crossing has no sign change, so bracketing cannot
find it."""
def f(x):
    return (x - 1.0) ** 2

for x in (0.9, 0.99, 1.0, 1.01, 1.1):
    print(f"x = {x:<6} f(x) = {f(x):.6e}  sign = "
          f"{'+' if f(x) > 0 else '0' if f(x) == 0 else '-'}")

print()
print("f is zero at x = 1 and positive on both sides, so no interval brackets it.")

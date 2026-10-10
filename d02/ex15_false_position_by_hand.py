"""The chord uses the function values, so the first guess is already better than a
midpoint."""
def f(x):
    return x ** 3 - 2 * x - 5

a, b = 2.0, 3.0
fa, fb = f(a), f(b)
mid = a + (b - a) / 2
chord = (a * fb - b * fa) / (fb - fa)

print("f(2) =", fa, "  f(3) =", fb)
print("bisection would try :", f"{mid:.12f}", " f =", f"{f(mid):+.6f}")
print("the chord crosses at:", f"{chord:.12f}", " f =", f"{f(chord):+.6f}")
print()
print("the chord lands nearer because f(3) is much "
      "larger than f(2), so the root is near 2.")

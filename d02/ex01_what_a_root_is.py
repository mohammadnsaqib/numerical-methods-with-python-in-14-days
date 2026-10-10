"""A root is where the function is zero, and a value near zero is not the same thing."""
import math

def f(x):
    return x ** 3 - 2 * x - 5

for x in (2.0, 2.09, 2.0945, 2.0945514815423265):
    print(f"x = {x:<20} f(x) = {f(x):+.15e}")

print()
print("the smallest f value here is at the last "
      "x, but none of these is proved to be a root.")

"""Newton's step is the tangent's crossing, and three steps of it can be printed in
full."""
def f(x):
    return x ** 3 - 2 * x - 5

def df(x):
    return 3 * x * x - 2

x = 3.0
print(f"{'step':>5} {'x':>20} {'f(x)':>14} {'slope':>10} {'next x':>20}")
for k in range(1, 5):
    fx, d = f(x), df(x)
    nxt = x - fx / d
    print(f"{k:>5} {x:>20.15f} {fx:>14.6e} {d:>10.4f} {nxt:>20.15f}")
    x = nxt

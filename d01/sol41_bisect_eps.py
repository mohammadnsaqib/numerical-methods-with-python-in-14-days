"""Problem 1.41: the threshold where 1 + x stops being 1, found by bisection."""
lo, hi = 0.0, 1.0                 # 1 + lo == 1 is true, 1 + hi == 1 is false
steps = 0
while True:
    mid = 0.5 * (lo + hi)
    if mid == lo or mid == hi:    # the interval is now one representable step wide
        break
    if 1.0 + mid == 1.0:
        lo = mid
    else:
        hi = mid
    steps += 1

EPS = 2.0 ** -52
print("bisection steps :", steps)
print("largest x with 1 + x == 1 :", f"{lo:.17e}")
print("smallest x with 1 + x != 1:", f"{hi:.17e}")
print("half an epsilon           :", f"{EPS / 2:.17e}")
print("the threshold is half an epsilon plus one step:", hi > EPS / 2)

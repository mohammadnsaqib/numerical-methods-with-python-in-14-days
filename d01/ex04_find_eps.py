"""Machine epsilon is not a constant to look up; it is a property that can be measured.
"""
import sys

e = 1.0
steps = 0
while 1.0 + e / 2.0 != 1.0:
    e = e / 2.0
    steps += 1

print("halvings needed :", steps)
print("measured epsilon:", e)
print("sys.float_info  :", sys.float_info.epsilon)
print("they agree      :", e == sys.float_info.epsilon)
print("epsilon as 2**-n:", e == 2.0 ** -52)

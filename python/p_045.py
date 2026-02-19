import numpy as np
import math



def is_pentagonal(x: int):
    if x < 0:
        return False
    d = 24*x + 1
    k = int(math.isqrt(d))
    return k * k == d and (k + 1) % 6 == 0

def is_hexagonal(x: int):
    d = 8 * x + 1
    k = int(math.isqrt(d))
    return k * k == d and (k + 1) % 4 == 0

def is_triangular(x: int):
    d = 8 * x + 1
    k = int(math.isqrt(d))
    return k * k == d and (k - 1) % 2 == 0

Number = 40756  # 40755 is known common value; search the next one
while not (is_hexagonal(Number) and is_pentagonal(Number) and is_triangular(Number)):
    Number += 1
    print(Number)
print(Number)

import math

def is_pentagonal(x: int) -> bool:
    if x < 0: return False
    d = 24*x + 1
    k = math.isqrt(d)
    return k*k == d and (k + 1) % 6 == 0

def is_hexagonal(x: int) -> bool:
    d = 8*x + 1
    k = math.isqrt(d)
    return k*k == d and (k + 1) % 4 == 0

# Iterate over hexagonal numbers (already triangular),
# and test pentagonal for the intersection.
n = 144  # because H_143 = 40755 is the given example, so start after it
while True:
    h = n*(2*n - 1)
    if is_pentagonal(h):
        print(h)
        break
    n += 1

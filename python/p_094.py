# Project Euler Problem 94
# Solution by Dominik Szombathy
# Date: 2026.02.13

# Solution = 518,408,346

from math import isqrt

def sum_perimeters(limit: int = 1_000_000_000) -> int:
    total = 0

    # Solutions (k,h) to k^2 - 3 h^2 = 1
    # Start from the fundamental nontrivial solution (2,1)
    k, h = 2, 1

    while True:
        added_any = False

        # b = a + 1
        if (1 + 2*k) % 3 == 0:
            a = (1 + 2*k) // 3
            b = a + 1
            p = 2*a + b  # = 3a + 1
            if p <= limit and b > 0:
                total += p
                added_any = True

        # b = a - 1
        if (2*k - 1) % 3 == 0:
            a = (2*k - 1) // 3
            b = a - 1
            p = 2*a + b  # = 3a - 1
            if p <= limit and b > 0:
                total += p
                added_any = True

        # If neither candidate can fit anymore, we can stop (k,h grow strictly).
        # a is about 2k/3, so perimeter about 2k; once 2k is past limit, we're done.
        if 2*k > limit + 10 and not added_any:
            break

        # Next (k,h): (k + h*sqrt(3)) *= (2 + sqrt(3))
        k, h = 2*k + 3*h, k + 2*h

    return total

print(sum_perimeters())  # 518408346

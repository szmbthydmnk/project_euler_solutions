# problem 91 - 2026.02.04 - Solution by Dominik Szombathy
# Difficulty level - 5
# Solution = 14234

# IDEA:
"""
There are 3 cases:
i)      the 90 degrees is at the origin
ii)     -||- is at Q
iii)    -||- is at P

Case i)
    This means that the sides of the triangle is on the axes of x and y. Goodie. there are 50 possibilities for Q and 50 for P ==> 50^2 such triangles.

Case ii)
    The vector pointing to Q (or P), call it vector_1 is perpendicular to the vector pointing from Q to P (or from P to Q), call it vector_2
    Take the scalar product of <v_1, v_2> = 0
    As the elements of these are defo integers, the product has no precision issues.

    It is enough to go through the coordinate space of Q (or P) then based on conditions that makes QP perpendicular to Q we can make steps
"""

# Helper functions

import math

def count_right_triangles(N: int = 50):
    total = N * N  # right angle at origin

    for x in range(N+1):
        for y in range(N+1):
            if x == 0 and y == 0:
                continue

            g = math.gcd(x, y)
            dx = y // g
            dy = x // g

            k1 = min((N - x) // dx if dx != 0 else 10**9,
                     y // dy if dy != 0 else 10**9)

            k2 = min(x // dx if dx != 0 else 10**9,
                     (N - y) // dy if dy != 0 else 10**9)

            total += k1 + k2

    return total

print(count_right_triangles(50))

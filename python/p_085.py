from math import comb
import numpy as np

def RectangleCount(n, m):
    return comb(n+1, 2) * comb(m+1, 2)

sizes = []

for N in range(1, 80):
    for M in range(N, 80):
        count = RectangleCount(N, M)
        sizes.append(count)
        print(f"N={N}, M={M} -> Rectangles={count - 2_000_000}")
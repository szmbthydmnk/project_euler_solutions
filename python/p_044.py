import math

def P(n):  # exact integer pentagonal
    return n*(3*n - 1)//2

def is_pentagonal(x: int):
    if x < 0:
        return False
    d = 24*x + 1
    k = int(math.isqrt(d))
    return k*k == d and (k + 1) % 6 == 0

Distances = []
N = 3000  # increase as needed
for i in range(2, N):
    Pi = P(i)
    for j in range(1, i):
        Pj = P(j)
        DM = Pi - Pj
        DP = Pi + Pj
        if is_pentagonal(DM) and is_pentagonal(DP):
            Distances.append(DM)

print(min(Distances) if Distances else None)

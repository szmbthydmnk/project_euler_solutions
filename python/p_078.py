# Coin partitions - Project Euler 78
# Find the least value of n for which p(n) is divisible by one million.

import sys
sys.setrecursionlimit(10000)

MODULO = 1_000_000
memo = {0: 1}

def CountPartitions(n: int) -> int:
    """
    Recursive computation of the partition function p(n) using Euler's pentagonal number theorem.
    Returns p(n) modulo MODULO for efficiency.
    """
    if n in memo:
        return memo[n]
    total = 0
    k = 1
    while True:
        pent1 = k * (3 * k - 1) // 2
        pent2 = k * (3 * k + 1) // 2
        if pent1 > n and pent2 > n:
            break
        sign = -1 if k % 2 == 0 else 1
        if pent1 <= n:
            total += sign * CountPartitions(n - pent1)
        if pent2 <= n:
            total += sign * CountPartitions(n - pent2)
        k += 1
    memo[n] = total % MODULO
    return memo[n]

if __name__ == "__main__":
    n = 1
    while True:
        if CountPartitions(n) == 0:
            print("Answer:", n)
            break
        n += 1
        
        
from sympy import factorint
print(factorint(28433))

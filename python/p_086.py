# Project Euler - 86 - Cuboid Route
# Solution by Dominik Szombathy 
# Date - 2026.02.18

# Solution: 1818

from math import isqrt

MAX_M = 2000                 # hard-coded precompute limit (covers the Euler target 1818) [web:1]
TESTCASES = [99, 100]        # hard-coded queries; prints 1975 and 2060 [web:9]
TARGET = 1_000_000           # Euler #86 threshold [web:1]

def pairs_count(m, s):
    # number of (a,b) with 1<=a<=b<=m and a+b=s
    if s <= m + 1:
        return s // 2
    return m - (s - 1) // 2

def build_prefix(max_m):
    pref = [0] * (max_m + 1)
    total = 0
    for m in range(1, max_m + 1):
        add = 0
        mm = m * m
        for s in range(2, 2 * m + 1):
            v = mm + s * s
            r = isqrt(v)
            if r * r == v:
                add += pairs_count(m, s)
        total += add
        pref[m] = total
    return pref

def first_m_exceeding(pref, target):
    for m in range(1, len(pref)):
        if pref[m] > target:
            return m
    return None

def main():
    pref = build_prefix(MAX_M)

    # Print testcase answers (one per line)
    for m in TESTCASES:
        print(pref[m])

    # Print Euler answer (first M with count > 1,000,000)
    m_ans = first_m_exceeding(pref, TARGET)
    print(m_ans)

if __name__ == "__main__":
    main()

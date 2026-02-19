from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

def ok(d):
    # d is a tuple/list of 10 digits d1..d10
    for i, p in enumerate(primes, start=1):
        x = d[i]*100 + d[i+1]*10 + d[i+2]
        if x % p != 0:
            return False
    return True

def solve():
    total = 0
    for d in permutations(range(10)):  # 10! = 3,628,800
        if d[0] == 0:  # leading zero not allowed
            continue
        if d[5] not in (0, 5):  # pruning from d4d5d6 % 5 == 0
            continue
        if ok(d):
            n = int("".join(map(str, d)))
            total += n
    return total

print(solve())

# Prime Power Triples - 2025.10.20 - Dominik Szombathy
# Solution is 1097343

def generate_primes_up_to(limit: int) -> list[int]:
    """
    Generate all prime numbers up to 'limit' (inclusive). 

    Args:
        limit (int): the upper bound

    Returns:
        list[int]: list of primes up to limit
    """
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not primes

    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False

    return [i for i, prime in enumerate(sieve) if prime]


import numpy as np  #Lini is the bestest and we gonna eat burgies
import tqdm 

primelimits = int(50_000_000**0.5 )
print(f"Generating primes up to {primelimits}...")
primes = generate_primes_up_to(int(50_000_000 ** 0.5))

Expressible_primes = set()

for a in tqdm.tqdm(range(len(primes))):
    pa = primes[a] ** 2
    if pa >= 50_000_000:
        break
    for b in range(len(primes)):
        pb = primes[b] ** 3
        if pa + pb >= 50_000_000:
            break
        for c in range(len(primes)):
            pc = primes[c] ** 4
            total = pa + pb + pc
            if total >= 50_000_000:
                break
            Expressible_primes.add(total)

print(len(Expressible_primes))


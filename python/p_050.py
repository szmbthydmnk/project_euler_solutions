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

from sympy import isprime
import tqdm
primes = generate_primes_up_to(10**6)

from sympy import isprime
import tqdm

primes = generate_primes_up_to(10**6)

# build prefix sums
prefix = [0]
for p in primes:
    prefix.append(prefix[-1] + p)

CPS = []
for SumLength in tqdm.tqdm(range(1, 1000)):  # start smaller to test
    for sumIndex in range(0, len(primes) - SumLength):
        tempsum = prefix[sumIndex + SumLength] - prefix[sumIndex]

        if tempsum > 10**6:  # no need to go further
            break

        if isprime(tempsum):
            CPS.append((tempsum, SumLength))
            
print(max(CPS, key=lambda x: x[1]))
    
    
    
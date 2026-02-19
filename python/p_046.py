
# INFO:
# A composite number is a positive integer greater than 1 that has more than two factors, meaning it can be formed by multiplying two smaller positive integers

import math
import numpy as np
from sympy import isprime

def is_compositeNumber(N: int) -> bool:
    """
    Determins whether the intput int is a composite number or not
    
    Args:
        N (int): number that will be checked
        
    Raises:
        TypeError: if the input is not an integer
        ValueError: if the value is negative
    """
    
    if not isinstance(N, (int, np.integer)):
        raise TypeError("Argument must be an integer")
    if N < 0:
        raise ValueError("Number is negative")
    
    N = int(N)  # ensure compatibility with sympy.isprime
    
    if N > 1 and not isprime(N):
        return True
    return False

# is_compositeNumber(10)


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

# print(generate_primes_up_to(10000))
PrimeLimit = 10 ** 4
primes = generate_primes_up_to(PrimeLimit)

Works = True
N = 3
while Works:
    if is_compositeNumber(N):
        N_check = False
        for p in [x for x in primes if x < N]: # education purposes only, breaking would be faster than creating a "limited" list each time.
            if np.floor(np.sqrt((N - p) / 2))**2 == (N - p)/2:  # this should be written in a separate function for clean code.
                N_check = True
            
        if not N_check:
            Works = False
        
        N += 2  # since the primes are generated, we could just check whether this is a prime or not by default, eliminating an unnecessary loop of while.
    else:
        N += 2

print(N)
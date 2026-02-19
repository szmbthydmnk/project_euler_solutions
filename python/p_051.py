
# Prime Digit replacements

import tqdm
from sympy import isprime
import numpy as np

def ReplaceDigits(OriginalNumber: int, ReplaceIndices: list, ReplaceNumber: int):
    Temp = list(str(OriginalNumber))
    for position in ReplaceIndices:
        Temp[position] = str(ReplaceNumber)    
    return int(''.join(Temp))

# print(ReplaceDigits(1234321, [2, 3, 4, 5], 9))

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

# 




Primes = generate_primes_up_to(10**7)


def repeated_digit_indices(Number: int):
    NumberString = str(Number)
    Indices = {}
    
    for i, d in enumerate(NumberString):
        Indices.setdefault(d, []).append(i)
    # keep only digits that appear more than once
    return {d: idxs for d, idxs in Indices.items() if len(idxs) > 1}

# rd = repeated_digit_indices(12112)



for p in tqdm.tqdm(Primes):
    RepeatedDigits = repeated_digit_indices(p)
    if len(RepeatedDigits) > 0:
        for key, value in RepeatedDigits.items():
            FamilySize = 0
            for ReplacementNumber in range(10):
                # skip leading zeros
                if value[0] == 0 and ReplacementNumber == 0:
                    continue
                candidate = ReplaceDigits(p, value, ReplacementNumber)
                if isprime(candidate):
                    FamilySize += 1
            if FamilySize > 7:
                print("Family size:", FamilySize, "prime:", p, "digit replaced:", key, "indices:", value) 
        
    
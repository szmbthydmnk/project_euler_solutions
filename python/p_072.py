# Ordered Fractions

import tqdm
import math
from sympy import isprime, factorint

def is_RPF(fraction):
    n, d = fraction
    while d:
        n, d = d, n % d
    return n == 1

def NumberOfGCD_Euler(N: int) -> int:
    factors = factorint(N)  # {prime: exponent}
    result = 1
    for p, exp in factors.items():
        result *= p**(exp-1) * (p-1)
    return result

NumberOfFractions = 0
for d in tqdm.tqdm(range(2, 1_000_001)):
    NumberOfFractions += NumberOfGCD_Euler(d)
print(NumberOfFractions)

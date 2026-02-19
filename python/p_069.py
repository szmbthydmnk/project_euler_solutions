# Totient Maximum

from sympy import isprime, factorint

def NumberOfGCD_Euler(N: int) -> int:
    factors = factorint(N)  # {prime: exponent}
    result = 1
    for p, exp in factors.items():
        result *= p**(exp-1) * (p-1)
    return result

ratio = 0
smallestN = 1
for n in range(1, 1_000_000):
    if n/NumberOfGCD_Euler(n) > ratio:
        ratio = n/NumberOfGCD_Euler(n)
        print(ratio)
        smallestN = n

print(smallestN)
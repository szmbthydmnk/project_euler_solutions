import numpy as np
from sympy import isprime
# b prím
# |a| < b + 1 --> 
# Prímek: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ...
#    1, 2, 2,  4,  2,  4,  2,  4,  6,
# n = 0 : f = b --> b prím
# n = 1 : f = 1 + a + b
# n = 2 : f = 4 +2a + b
# n = 3 : f = 9 +3a + b


def euler27():
    
    MaxConsecutivePrimes = 0
    
    for b in range(1001):
        if isprime(b):
            print(b)
            for a in np.arange(-b-1, 1000):
                NumberOfPrimes = 0
                n = 0
                while isprime(n**2 + a*n + b):
                    NumberOfPrimes += 1
                    n += 1
                if NumberOfPrimes > MaxConsecutivePrimes:
                    MaxConsecutivePrimes = NumberOfPrimes
                    Parameters = [a, b]
    return [MaxConsecutivePrimes, Parameters]

Primes, Param = euler27()
print(Primes)
print(Param)

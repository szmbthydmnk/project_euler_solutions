from math import gcd
import time
from sympy import isprime, factorint
from tqdm import tqdm

def is_RelativePrime(x: int, y: int) -> bool:
    """
    Determine whether two integers are relatively prime (coprime).

    Args:
        x (int): First integer.
        y (int): Second integer.

    Returns:
        bool: True if x and y are coprimes, False otherwise.

    Raises:
        TypeError: If either x or y is not an integer.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both arguments must be integers.")
    
    return gcd(x, y) == 1

def is_Permutation(x: int, y: int) -> bool:
    """
    Determines whether two integers are permutation of each other.
    
    Args:
        x (int): First integer 
        y (int): Second integer
    
    Raises:
        TypeError: If either x or y is not an integer
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both arguments must be integers")
    
    return sorted(str(x)) == sorted(str(y))

def NumberOfGCD_Euler(N: int) -> int:
    factors = factorint(N)  # {prime: exponent}
    result = 1
    for p, exp in factors.items():
        result *= p**(exp-1) * (p-1)
    return result
    
    

from sympy import primerange

phi = []
n_list = []
LIMIT = 10**7 + 1
primes = list(primerange(2, int(2**16)))
for i, p in tqdm(enumerate(primes)):
    for q in primes[i:]:
        N = p * q
        if N >= LIMIT:
            break
        phi_N = (p - 1) * (q - 1)
        if is_Permutation(N, phi_N):
            phi.append((N, phi_N))
            n_list.append(N)
    
import matplotlib.pyplot as plt
import numpy as np

ratios = [N / phi_N for N, phi_N in phi]
min_index = np.argmin(ratios)
best_N, best_phi_N = phi[min_index]
print("N with minimum N/phi(N):", best_N)
print("Minimum ratio:", best_N / best_phi_N)
# Observations:
# - If n is even, then the number of checks we have to do is halved.
# - 1 and n-1 is always a given gcd
# - the ratio of n/\phi(n) only need to be stored for a permutation of n
# - if a number is a prime, then we already know it is a relative prime as well.
# - gcd(N, p) =\= 1 -> gcd(N, k*p) =\= 1
# - gcd(N, p) = 1 -> gcd(N, p^k) = 1
# - gcd(N, r) = 1 if r is a prime

# phi = []
# 
# for n in tqdm(range(2, 10**4)):
#     #print("n = ", n)
#     if n % 2 == 0:
#         candidates = list(range(2, n, 1))
#         #print("Candidates = ", candidates)
#     elif isprime(n):
#         candidates = []
#         print("N is prime!", n)
#     else:
#         candidates = list(range(2, n, 2))
#         #print("Candidates = ", candidates)
#     
#     
#     relativePrimes = []
#     
#     for p in candidates[:]:
#         #print("p = ", p)
#         if is_RelativePrime(p, n):
#             relativePrimes.append(p)
#             k = 1
#             while p**k < n:
# 
#                 if p**k in candidates:
#                     candidates.remove(p**k)
#                     relativePrimes.append(p ** k)
#                     k += 1
#                 else:
#                     k += 1
#                 
#         else:
#             k = 1
#             while p * k < n:
#                 if p * k in candidates:
#                     candidates.remove(p * k)
#                 
#                 k += 1
#     
#     phi_c = len(set(relativePrimes)) + 1
#     if is_Permutation(phi_c, n):
#         phi.append(len(set(relativePrimes)) + 1)           
# 
# 
# print(phi)
# #print(relativePrimes)
plt.plot(n_list, np.array(ratios) - 1)
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('N / phi(N) - 1 (log scale)')
plt.title('Ratio of N to phi(N) minus 1 for Permutations')
plt.show()
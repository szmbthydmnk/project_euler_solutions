# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import numpy as np

def euler10(N):
    array = [True] * (N+1)
    array[0] = False
    array[1] = False
    # ruling out all multiples of a prime number
    for i in range(int(np.sqrt(N))+1):
        if array[i]:
            for j in range(i**2, len(array), i):
                array[j] = False
    primes = 0
    for i in range(len(array)):
        if array[i]:
            primes += i
    return primes

print(euler10(2000000))

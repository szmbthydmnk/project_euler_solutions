# problem 77 - 2026.02.04 - Solution by Dominik Szombathy
# Difficulty level - 4
# Solution = 71

# IDEA
"""
Initial considerations:
- Terms in the sum are interchangable (commutative) therefore 2 + 3 and 3 + 2 are the same sum.
- If the number is a prime, then the number of ways must be at least 1
- My guess would be that every number (if N > 1) can be summed up in some way or another.

Approach:
M is a list with elements (int) telling us how many ways can we sum up a certain number.

0 can be summed up in 1 way
1 can be summed up in 0 way
2 can be summed up in 1 way as:     2
3 can be summed up in 1 way as:     3
4 can be summed up in 1 way as:     2 + 2 
5 can be summed up in 2 ways as:    2 + 3; 5
6 can be summed up in 2 ways as:    2 + 2 + 2; 3 + 3
…

Therefore:
M[0] = 1
M[1] = 0
M[2] = 1
…

1) We check whether the i-th number is a prime (if it is then the number of ways is M[i] = 1, else M[i] = 0)
2) We generate primes up until that number {p_i}, where p_i <= i
3) substract each p_i from i and check M[i - p_i] if i - p_i is positive then add that number to M[i] 
"""

import math

# Helper functions
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_next_prime():
    current = 2
    while True:
        if is_prime(current):
            yield current
        current += 1

# Solution:
def solution() -> None:

    # Number of sums limit
    number_of_sums_limit = 5_000

    number_of_sums = [0]

    # Prime generator
    primes = []
    next_prime = generate_next_prime()
    primes.append(next(next_prime))     # we append 2 as the first prime
    #print(primes)
    
    number = 2
    
    while number_of_sums[-1] < number_of_sums_limit:
        if number > primes[-1]:
            primes.append(next(next_prime))
            print(primes)

        
        number_of_sums = [0] * (number + 1)
        number_of_sums[0] = 1
        number_of_sums[1] = 0

        for p in primes:
            for s in range(p, number + 1):
                number_of_sums[s] += number_of_sums[s - p]
        
        number += 1
    
    print(number - 1, number_of_sums)

solution()



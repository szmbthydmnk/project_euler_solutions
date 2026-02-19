from itertools import permutations

# Generate 4-digit primes
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(1000, limit + 1) if sieve[i]]

primes = generate_primes(9999)
prime_set = set(primes)

# Group primes by sorted digits
from collections import defaultdict
groups = defaultdict(list)
for p in primes:
    key = ''.join(sorted(str(p)))
    groups[key].append(p)

# Find sequences
for key, numbers in groups.items():
    if len(numbers) < 3:
        continue
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            diff = numbers[j] - numbers[i]
            third = numbers[j] + diff
            if third in numbers:
                seq = (numbers[i], numbers[j], third)
                if seq != (1487, 4817, 8147):
                    print("Answer sequence:", seq)
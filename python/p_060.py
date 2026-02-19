from sympy import isprime
import numpy as np
import tqdm
import networkx as nx

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


def ConcatanateNumbers(a: int, b: int):
    return int(str(a) + str(b))


PrimeLimit = 30000
Primes = generate_primes_up_to(PrimeLimit)

G = nx.Graph()
# Build the graph from your connections
for i in tqdm.tqdm(range(len(Primes))):
    for j in range(i + 1, len(Primes)):
        if isprime(ConcatanateNumbers(Primes[i], Primes[j])) and isprime(ConcatanateNumbers(Primes[j], Primes[i])):
            G.add_edge(Primes[i], Primes[j])
# %%
# G is already built in your code
cliques_of_5 = [clique for clique in nx.find_cliques(G) if len(clique) == 2]

print(f"Number of 5-cliques found: {len(cliques_of_5)}")
for clique in cliques_of_5:
    print(sorted(clique), "sum:", sum(clique))
#
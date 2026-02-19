# problem: Project Euler 58 - Spiral Primes

from sympy import isprime
import numpy as np

ratio = []
M = 10**5
diagonals = np.zeros((4, M), dtype=int)
for layer in range(2, M):
    print("Layer = ", layer)
    for k in range(1, 5):
        if isprime((2*layer - 1)**2 - k*(2*layer - 2)):
            print((2*layer - 1)**2 - k*(2*layer - 2))
            diagonals[k-1][layer] = 1
    
    if np.sum(diagonals) / (4*layer - 3) < 0.1:
        print("Last layers side length = ", 2*layer - 1)
        break

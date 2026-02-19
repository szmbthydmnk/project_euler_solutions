# Digit Factorial Chains

# Problem 74

import math as m
import tqdm as t

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def DigitFacotiral(n):
    return sum(factorial(int(i)) for i in str(n))

def ChainLength(n):
    NumberExplored = {n}
    while True:
        n = DigitFacotiral(n)
        if n in NumberExplored:
            return len(NumberExplored)
        if len(NumberExplored) > 60:
            return 61
        NumberExplored.add(n)

Count = 0
for i in t.tqdm(range(1, 1_000_000)):
    if ChainLength(i) == 60:
        Count += 1
print(Count)



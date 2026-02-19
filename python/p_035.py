import itertools
from sympy import isprime
from tqdm import tqdm

def get_circular_combinations(Number):
    digits = [int(d) for d in str(Number)]
    Combinations = []

    for i in range(len(digits)):
        rotated_digits = digits[i:] + digits[:i]

        if rotated_digits[0] != 0:
            Combinations.append(int("".join(map(str, rotated_digits))))
    
    return Combinations

def consist_even_digit(Number):
    digit_str = str(Number)
    for digit in str(Number):
        if int(digit) % 2 == 0 and int(digit) != 0:
            return True
    return False

NumberOfCircularPrimes = 4      # I won't check the number 2 in the for loop.
for N in tqdm(range(10, 1000000), desc="Processing numbers"):
    if consist_even_digit(N) == False:
        if isprime(N):
            Combinations = get_circular_combinations(N)
            k = 1
            for i in range(len(Combinations)):
                if isprime(Combinations[i]):
                    k *= 1
                else:
                    k *= 0
            if k == 1:
                print(N)
            NumberOfCircularPrimes += k
            

print(NumberOfCircularPrimes)
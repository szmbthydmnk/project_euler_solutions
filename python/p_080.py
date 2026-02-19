# Square Root Digital Expansion


import tqdm as t
import math
import collections
L = 100

def is_quare(n):
    r = int(math.sqrt(n))
    return r * r == n


def digit_by_digit_sqrt(n : int, precision: int) -> list[int]:
    NumberPairs = []
    n_str = str(n)
    if len(n_str) % 2 == 1:
        n_str = '0' + n_str

    for i in range(0, len(n_str), 2):
        NumberPairs.append(int(n_str[i:i + 2]))
    
    for _ in range(precision):
        NumberPairs.append(0)

    NumberSqrt = []
    Remainder = 0
    Root = 0
    for pair in NumberPairs:
        Remainder = Remainder * 100 + pair

        NextDigit = 0

        Divisor = Root * 20
        for k in range(9, -1, -1):
            if (Divisor + k) * k <= Remainder:
                NextDigit = k
                break
        NumberSqrt.append(NextDigit)
        Remainder -= (Divisor + NextDigit) * NextDigit
        Root = Root * 10 + NextDigit
    return NumberSqrt


Sum = 0 
for N in range(1, L + 1):
    if not is_quare(N):
        digits = digit_by_digit_sqrt(N, 100)
        Sum += sum(digits[:100])

print(Sum)


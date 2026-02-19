# Project Euler - Problem 100
# Solution by Dominik Szombathy
# Date: 2026.01.07
# Solution: 756872327473
import math

def two_blue_disc_probability(blue_discs: int, other_discs: int) -> float:

    probability = 1
    no_all_discs = blue_discs + other_discs
    probability = (blue_discs**2 - blue_discs)/(no_all_discs**2 - no_all_discs)


    return probability

def next_discs(blue_discs: int, all_discs: int) -> list[int]:
    return [3*blue_discs + 2*all_discs - 2, 4*blue_discs + 3*all_discs - 3]

blue_discs = 3
all_discs = 4
while all_discs < 10**12:
    blue_discs, all_discs = next_discs(blue_discs, all_discs)

print(blue_discs, all_discs)
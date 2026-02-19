# Ordered Fractions

import tqdm
import math

def is_RPF(fraction):
    n, d = fraction
    while d:
        n, d = d, n % d
    return n == 1

ListOfFraction = []
Numbers = 0
for d in tqdm.tqdm(range(1_000_001, 0, -1)):
    n = math.floor(3*d / 7)
    fraction = [n, d]
    if is_RPF(fraction):
        if fraction[0]/fraction[1] < 3/7 and fraction[0]/fraction[1] > Numbers:
            Numbers = fraction[0]/fraction[1]
            ListOfFraction = fraction
            break
            

print(Numbers - 3/7, ListOfFraction)

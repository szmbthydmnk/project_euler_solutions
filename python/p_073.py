# Counting Fractions in a Range:

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
for d in tqdm.tqdm(range(1, 12_001)):
    for n in range(math.floor(d / 3), math.ceil(d / 2)):
        fraction = [n, d]
        if is_RPF(fraction) and fraction[0]/fraction[1] > 1/3 and fraction[0]/fraction[1] < 1/2:
            Numbers += 1
            

print(Numbers)

# Combinatorial selections - P.E. 53
import tqdm
import math
Counter = 0

for n in tqdm.tqdm(range(1, 101)):
    for r in range(0, n+1):
        if math.comb(n, r) > 1_000_000:
            Counter += 1
print(Counter)
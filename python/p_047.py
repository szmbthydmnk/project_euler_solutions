from sympy import isprime, factorint
import tqdm

sequence = 0
for n in tqdm.tqdm(range(10**5, 10**6)):
    if len(list(factorint(n).items())) == 4:
        sequence += 1
    else:
        sequence = 0
    
    if sequence == 4:
        print(n - 3)
        break
# Singular Integer Right Triangles

import tqdm as t
import math 
import collections 
L = 1500000

solutions = collections.defaultdict(int)

for m in t.tqdm(range(2, L)):
    for n in range(1, m):
        if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
        
            perimiter = a + b + c

            if perimiter > L:
                break

            k = 1
            while k * perimiter <= L+1:
                solutions[k * perimiter] += 1
                k += 1
        

result = sum(1 for v in solutions.values() if v == 1)
print(result)



import math
from tqdm import tqdm

def find_divisors(N: int) -> list[int]:
    divisors = [1]
    for d in range(2, int(math.sqrt(N)) + 1):
        if N % d == 0:
            divisors.append(d)
            if d * d != N:
                divisors.append(int(N / d))
    
    return sorted(divisors)

longest_chain = 1
smallest_member = 0
visited = set()
for N in tqdm(range(1, 1_000_000)):
    chain = [N]
    if N in visited:
        continue
    
    divisor_sum = sum(find_divisors(N))
    #print(divisor_sum, find_divisors(N))
    while divisor_sum <= 1_000_000 and divisor_sum not in chain and divisor_sum > 0:
        chain.append(divisor_sum)
        #print(chain)

        divisor_sum = sum(find_divisors(divisor_sum))
        #print(divisor_sum, find_divisors(divisor_sum))

    chain.append(divisor_sum) 

    for x in chain:
        visited.add(x)
        
    if len(chain) > longest_chain and N in chain[1:]:
        longest_chain = len(chain)
        smallest_member = min(chain)
        


print(longest_chain, smallest_member)


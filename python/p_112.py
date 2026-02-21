# Project Euler - 112 - Bouncy Numbers
# Solution by Dominik Szombathy 
# Date - 2026.02.21
# Difficulty: 2

# Solution: 1587000

def is_bouncy(number: int) -> bool:
    num_str = str(number)
    decreasing = 0
    increasing = 0
    base = num_str[0]
    for n in num_str[1::]:
        if int(n) > int(base):
            increasing += 1
            base = n
        elif int(n) < int(base):
            decreasing += 1
            base = n
        
        if increasing >= 1 and decreasing >= 1:
            return True
    
    return False        

bouncy_number_count = 0
N = 100
while bouncy_number_count/N < 0.99:
    N += 1
    #if is_bouncy(N):
    #    print(N)
    bouncy_number_count += 1 if is_bouncy(N) else 0
    
print(N)

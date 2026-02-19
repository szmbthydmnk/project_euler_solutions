# Lychrel Numbers - P.E. 55
import tqdm

def ReverseAndAdd(N: int):
    return int(str(N)[::-1]) + N

def is_Palindrome(Number: int):
    return str(Number) == str(Number)[::-1]

def is_Lychrel(Number: int):
    Limit = 50  # Project Euler 55 specifies 50 iterations
    for _ in range(Limit):
        Number = ReverseAndAdd(Number)
        if is_Palindrome(Number):
            return False  # Not a Lychrel
    return True  # No palindrome found → Lychrel
    
Number_of_Lychrel_numbers = 0    
for N in tqdm.tqdm(range(0, 10_001)):
    if is_Lychrel(N):
        Number_of_Lychrel_numbers += 1
        
print(Number_of_Lychrel_numbers)
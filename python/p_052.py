# Permuted Multiples - P.E. 52
import tqdm 

def CheckDigits(X: int, Y: int):
    return sorted(str(X)) == sorted(str(Y))

# print(CheckDigits(123, 231))

for N in tqdm.tqdm(range(10**1, 10**7)):
    for M in range(1, 7):
        if not CheckDigits(N, M * N):
            break
        elif M == 6:
            print(N)
            break
    
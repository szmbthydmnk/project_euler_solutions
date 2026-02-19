# Square digit chains
import tqdm 

def ChainNumberStep(N: int):
    Number = 0

    for digit in str(N):
        Number += int(digit)**2
    
    return Number
EndsUpIn89 = 0
SetOf1  = set()
SetOf89 = set()
for i in tqdm.tqdm(range(1, 10_000_000)):
    Number = i
    TempSet = {Number}

    while not (Number == 1 or Number == 89):
        Number = ChainNumberStep(Number)
        TempSet.add(Number)
        #print(Number)
        if Number == 89 or Number in SetOf89:
            EndsUpIn89 += 1
            SetOf89.update(TempSet)
            break
        elif Number in SetOf1:
            SetOf1.update(TempSet)
            break

print(EndsUpIn89 + 1)


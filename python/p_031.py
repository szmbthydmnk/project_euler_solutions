#In the United Kingdom the currency is made up of pound (£) and pence (p).
#There are eight coins in general circulation:

#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#It is possible to make £2 in the following way:

#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?

Coins = [1, 2, 5, 10, 20, 50, 100, 200]

import numpy as np
import time

def euler31(PenceAmount: int, Coins):
    Ways = np.zeros(PenceAmount + 2)
    if PenceAmount < 0:
        return 0
    if PenceAmount == 0:
        return 1
    else:
        Ways[1] = 1
        for CoinInd in Coins:
            for CountingInd in range(CoinInd, PenceAmount + 1):
                Ways[CountingInd + 1] += Ways[CountingInd + 1 - CoinInd]
        return Ways[-1]
    
print(euler31(200, Coins))
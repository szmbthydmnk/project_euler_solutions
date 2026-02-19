# 1/2 = 0.5
# 1/4 = 0.5 * 0.5
# 1/3 = 0.33333
import numpy as np
#import sys
from sympy import isprime, nextprime

#sys.setrecursionlimit(1500)
#print(sys.getrecursionlimit())

def ManualDivision(a, b, RemainderList):
    Divident, Remainder = divmod(a, b)
    if (Remainder != 0 and (Remainder not in RemainderList)):
        RemainderList.append(Remainder)
        return ManualDivision(10 * Remainder, b, RemainderList)
    else:
        return len(RemainderList)

#def ManualDivision(a, b, RemainderList, MaxListLength):
#    Divident, Remainder = divmod(a, b)
#    if (Remainder != 0 and (Remainder not in RemainderList)):
#        RemainderList.append(Remainder)
#        return ManualDivision(10 * Remainder, b, RemainderList, MaxListLength)
#    else:
#        if len(RemainderList) > MaxListLength:
#            MaxListLength = len(RemainderList)
#        if nextprime(b) < 160:
#            b = nextprime(b)
#            return ManualDivision(a, b, [], MaxListLength)
#        else:
#            return MaxListLength     

def euler26():
    a = 1
    ListLengthMax = [0, 0]
    for b in range(1, 1000):
        ListLength = ManualDivision(a, b, [])
        if ListLength > ListLengthMax[0]:
            ListLengthMax = [ListLength, b]
    return ListLengthMax

#print(ManualDivision(1, 1, [], 0))
print(euler26())
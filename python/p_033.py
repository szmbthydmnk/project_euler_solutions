from math import gcd

def Digit_Cancelling(Nom, Denom):
    Digits_Nom = list(str(Nom))
    Digits_Denom = list(str(Denom))

    for i in range(len(Digits_Nom)):
        for j in range(len(Digits_Denom)):
            if Digits_Nom[i] == Digits_Denom[j] and Digits_Nom[i] != '0':

                temp_Nom    = Digits_Nom[len(Digits_Nom) - 1 - i]
                temp_Denom  = Digits_Denom[len(Digits_Denom) - 1 - j]

                if temp_Nom != 0 and (int(temp_Nom) * Denom == int(temp_Denom) * Nom):
                    return True
    return False

Numerator   = 1
Denominator = 1

for n in range(11,100):# range(10, 100):
    for d in range(n + 1, 100): # range(n + 1, 100):

        if Digit_Cancelling(n, d):
            Numerator *= n
            Denominator *= d

gcd_number = gcd(Numerator, Denominator)
print(Denominator/gcd_number)
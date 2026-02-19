# Convergents of e

n = 100
terms = [2]
k = 1
while len(terms) < n:
    terms += [1, 2*k, 1]
    k += 1
terms = terms[:n]

h1, h2 = 1, terms[0]
k1, k2 = 0, 1

for a in terms[1:]:
    h1, h2 = h2, a*h2 + h1
    k1, k2 = k2, a*k2 + k1

numerator = h2
digit_sum = sum(int(d) for d in str(numerator))
print(digit_sum)
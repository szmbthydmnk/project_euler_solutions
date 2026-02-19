#bruteforce will do the job, but we can do better
def euler6_1(N):
    sum1 = (sum(i for i in range(1,N+1)))**2
    sum2 = sum(j**2 for j in range(1,N+1))

    return sum1 - sum2
#Using some math here:
# sum from 1 to N the natural numbers: (N/2)*(N+1)
# suming n^2 from 1 to N gives (2N^3 + 3N^2 + N)/6 if one would consider summing up (k - 1)^3
def euler6_2(N):
    s1 = (N*(N+1)/2)**2
    s2 = N*(N+1)*(2*N + 1)/6
    return int(s1 - s2)
print(euler6_1(100))
print(euler6_2(100))

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13. What is the 10 001st prime number?

def euler7(N):
    #10.001th prime number oh boi
    primes = [2]
    num = 3
    while len(primes) < N:
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
        num += 2    #one could exclude all even numbers from prime checks

    return primes[-1]

print(euler7(10001))

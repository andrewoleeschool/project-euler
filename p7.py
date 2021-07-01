# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

n = 10001

primes = [2]

i = 3
while len(primes) < n:
    prime = True
    for p in primes:
        if i % p == 0:
            prime = False
            break
    if prime:
        primes.append(i)
    i += 1

print(primes[-1])

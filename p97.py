# The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

# Find the last ten digits of this prime number.

a = 28433
b = 2
c = 7830457
N = int(1e10)

n = 1
while c > 0:
    if c % 2 == 1:
        n *= b
    c = c // 2
    b *= b
    n = n % N

print((a * n + 1) % N)

# 8739992577
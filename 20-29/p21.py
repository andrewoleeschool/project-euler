# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math

n = 10000

def sumDivs(n: int) -> int:
    nCpy = n
    m = 2
    sumDiv = 1
    while n > 1:
        e = 0
        while n % m == 0:
            n //= m
            e += 1
        if e > 0:
            sumDiv *= (m**(e + 1) - 1) // (m - 1)
        m += 1
    return sumDiv - nCpy

def amicable(n: int) -> bool:
    m = sumDivs(n)
    return m != n and sumDivs(m) == n

sumAm = 0
for i in range(2, n):
    if amicable(i):
        print(i)
        sumAm += i

print(sumAm)
    
# 31626
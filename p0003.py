# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

n = 600851475143

m = 2
max = 1
while n > 1:
    if n % m == 0:
        max = m if m > max else max
        n /= m
        m = 2
    else:
        m += 1

print(max)

# 6857
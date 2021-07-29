# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

import numpy as np
import math

n = 1000000

m = math.isqrt(n * 10) + 1
seive = np.full(n * 10, True, bool)
seive[0] = False
seive[1] = False

for i in range(2, m):
    if seive[i]:
        for j in range(2 * i, n * 10, i):
            seive[j] = False


def circular(n: int) -> bool:
    if not seive[n]:
        return False
    nStr = str(n)
    rot = nStr[1:] + nStr[0]
    while rot != nStr:
        if not seive[int(rot)]:
            return False
        rot = rot[1:] + rot[0]
    return True

numCirc = 0
for i in range(2, n):
    if circular(i):
        numCirc += 1

print(numCirc)

# 55
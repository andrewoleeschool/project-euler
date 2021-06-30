# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import numpy as np
import math


n = 20
n += 1
m = math.isqrt(n) + 1

seive = np.full(n, True, bool)
seive[0] = False
seive[1] = False

for i in range(2, m):
    if seive[i]:
        for j in range(2 * i, n, i):
            seive[j] = False

prod = 1
for i in range(2, n):
    if seive[i]:
        prod *= i ** math.floor(math.log(n - 1, i))

print(prod)
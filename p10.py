# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import numpy as np
import math

n = 2000000
m = math.isqrt(n) + 1

seive = np.full(n, True, bool)
seive[0] = False
seive[1] = False

for i in range(2, m):
    if seive[i]:
        for j in range(2 * i, n, i):
            seive[j] = False

sum = 0
for i in range(n):
    if seive[i]:
        sum += i

print(sum)

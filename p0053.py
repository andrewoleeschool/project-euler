# There are exactly ten ways of selecting three from five, 12345: 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# It is not until , that a value exceeds one-million: 23C10=1144066

# How many, not necessarily distinct, values of nCr for 1<=n<=100 are greater than one-million?

import math

N = 1000000

combs = 0
for n in range(1, 101):
    m = n // 2 + 1
    for r in range(1, m):
        nCr = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        if nCr > N:
            combs += 2 * (m - r)
            if n % 2 == 0 and r != m:
                combs -= 1
            break

print(combs)

# 4075
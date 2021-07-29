# The following iterative sequence is defined for the set of positive integers: n → n/2 (n is even) n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# note: Once the chain starts the terms are allowed to go above one million.

import numpy as np

N = 1000000

chains = np.full(N, 0)
chains[1] = 1

for i in range(2, N):
    n = i
    chain = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n < N and chains[n] != 0:
            chain += chains[n]
            break
        chain += 1
     
    chains[i] = chain

print(np.argmax(chains))

# 837799
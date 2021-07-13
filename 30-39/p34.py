# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

import math

dsum = 0
for i in range(10, 1000000):
    dfact = sum(map(math.factorial, map(int, str(i))))
    if dfact == i:
        dsum += i

print(dsum)

# 40730
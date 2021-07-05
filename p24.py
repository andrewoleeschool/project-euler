# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math

n = 1000000
base = 10

digits = [i for i in range(base)]
result = ""

n -= 1
for i in range(base):
    fact = math.factorial(base - i - 1)
    temp = n // fact
    result += str(digits[temp])
    digits.pop(temp)
    n -= temp * fact

print(result)

# 2783915460
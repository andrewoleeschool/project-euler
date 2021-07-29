# In the following equation x, y, and n are positive integers.

# 1/x + 1/y = 1/n

# For n = 4 there are exactly three distinct solutions:

N = 1000

def divisors(n: int) -> int:
    m = 2
    divs = 1
    while n > 1:
        e = 1
        while n % m == 0:
            n /= m
            e += 2
        divs *= e
        m += 1
    return divs

n = 150000
divs = 0

while divs < 2 * N - 1:
    n += 1
    divs = divisors(n)

print(n)

# 180180

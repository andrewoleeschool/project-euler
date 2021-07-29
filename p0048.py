# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def modPow(a: int, b: int) -> int:
    N = int(1e10)
    n = 1
    while b != 0:
        if b % 2 == 1:
            n *= a % N
        a *= a % N
        b //= 2
    return n % N

sumS = 0
for i in range(1, 1001):
    sumS += modPow(i, i)

print(sumS % int(1e10))

# 9110846700
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sumMultiples(n: int, m: int) -> int:
    x = (n - 1) // m
    return (x + 1) * x * m // 2

n = 1000
m1 = 3
m2 = 5

res = sumMultiples(n, m1) + sumMultiples(n, m2) - sumMultiples(n, m1 * m2)
print(res)
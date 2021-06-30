# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...10^2=385

# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640

n = 100

sumOfSq = n * (n + 1) * (2 * n + 1) / 6
sqOfSum = (n * (n + 1) / 2) ** 2

print(sqOfSum - sumOfSq)
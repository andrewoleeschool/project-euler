# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

n = 4000000
sum = 0

fib0 = 1
fib1 = 2

while fib1 < n:
    if fib1 % 2 == 0:
        sum += fib1
    fib0, fib1 = fib1, fib0 + fib1

print(sum)
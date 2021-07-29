# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

count = 0

a = 1
b = 1

digPow = str(a**b)
a = 1
while len(digPow) <= b:
    if len(digPow) == b:
        count += 1
    digPow = str(a**b)
    a += 1
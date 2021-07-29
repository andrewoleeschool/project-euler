# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

# Hence the first 12 terms will be:

# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

a = 1
b = 1
i = 1

while len(str(a)) < 1000:
    a, b = b, a + b
    i += 1

print(i)

# 4782
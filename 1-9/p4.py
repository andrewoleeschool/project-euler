# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

for i in range(999, 900, -1):
    for j in range(999, 900, -1):
        if palindrome(i * j):
            print(i * j)
            exit()

# 906609
# Not guarenteed to be largest, but seems to arrive at correct result for 3 digits
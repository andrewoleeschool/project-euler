# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# It is possible to make £2 in the following way: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?

def count(coins: 'list[int]', m: int, n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n > 0:
        return 0
    return count(coins, m - 1, n) + count(coins, m, n - coins[m - 1])

coins = [1, 2, 5, 10, 20, 50, 100, 200]
n = 200

print(count(coins, len(coins), n))

# 73682
# Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

# For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

# For 3 ≤ a ≤ 1000, find ∑ rmax.

def rmax(a: int) -> int:
    rmx = 0
    for n in range(a):
        r = (2 * n * a) % (a**2)
        if r > rmx:
            rmx = r
    return rmx

sumR = 0
for a in range(3, 1001):
    sumR += rmax(a)

print(sumR)

# 333082500
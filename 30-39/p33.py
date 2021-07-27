# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

dcf = []

for i in range(10, 100):
    for j in range(i + 1, 100):
        iDigits = list(map(int, str(i)))
        jDigits = list(map(int, str(j)))
        if iDigits[1] == 0 and jDigits[1] == 0:
            continue
        if iDigits[0] == jDigits[0] and i * jDigits[1] == j * iDigits[1]:
            dcf.append((i, j))
        if iDigits[0] == jDigits[1] and i * jDigits[0] == j * iDigits[1]:


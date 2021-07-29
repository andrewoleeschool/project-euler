# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def numToWord(n: int) -> str:
    numWordDict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        1000: "one thousand"
    }

    if n in numWordDict:
        return numWordDict[n]

    numWord = ""
    if n > 99:
        numWord += numWordDict[n // 100] + " hundred"
        n = n % 100
        if n != 0:
            numWord += " and "

    if n in numWordDict:
        return numWord + numWordDict[n]

    if n > 19:
        numWord += numWordDict[(n // 10) * 10]
        n = n % 10
        if n != 0:
            numWord += " "

    if n in numWordDict:
        return numWord + numWordDict[n]

    return numWord

sumLetters = 0
for i in range(1, 1001):
    sumLetters += len(numToWord(i).replace(" ", ""))

print(sumLetters)

# 21124
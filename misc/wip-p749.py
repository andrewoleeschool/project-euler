# A positive integer, n, is a near power sum if there exists a positive integer, k, such that the sum of the kth powers of the digits in its decimal representation is equal to either n+1 or n−1. For example 35 is a near power sum number because 3^2+5^2=34.

# Define S(d) to be the sum of all near power sum numbers of d digits or less. Then S(2)=110 and S(6)=2562701.Find S(16).

def nearPowerSum(n: int) -> bool:
    digits = list(map(int, str(n)))
    for k in range():
        for digit in digits:


    return True

nearPowerSum(45)
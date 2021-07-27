# For non-negative integers m, n, the Ackermann function is defined as follows: 

#  For example A(1,0)=2, A(2,2)=7 and A(3,4)=125. 

# Find Find \sum_{n=0}^6 A(n,n) and give your answer mod 14^8.

def ackermann(m: int, n: int) -> int:
    stack = [m]
    while stack:
        print(len(stack))
        m = stack.pop()
        if m == 0:
            n += 1
        elif n == 0:
            stack.append(m - 1)
            n = 1
        else:
            stack.append(m - 1)
            stack.append(m)
            n -= 1 
    return n

print(ackermann(4, 4))
"""
Create a recursive function to compute a summation.

summation(n) = n + summation(n-1)


Example: summation(3)
3 + summation(2)
    2 + summation(1)
        1 + summation(0)

returns 6
"""






def summation(n):
    if n == 0:
        return 0
    else:
        return n + summation(n-1)
result = summation(4)
print("result is", result)

defloopSum(n):
    total = 0
    for i in range(n+1):
        total = total + i
    return total

"""
Create a recursive function to compute factorials.

factorial(n) = n * factorial(n-1)
factorial(0) = 1

factorial(4) = 4 * factorial(3)
                    3 * factorial(2)
                        2 * factorial(1)
                            1 * factorial(0)
                                1
result is 24

Key Characteristics for recursive functions:
1. There must be one or more base cases where recursion ends
2. All recursive calls must eventually end up at a base case
"""

def factorial(n):
    #base cases
    if n == 0:
        return 1
    #recursive case
    else:
        return n * factorial(1-n)
result = factorial(3)
print("result is", result)


def loopFact(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

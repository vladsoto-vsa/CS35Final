"""
Here are some example problems.  Write a RECURSIVE solution to each one.

Remember that every recursive function must have at least one base case
where no recursion occurs.
"""

from math import sqrt

def main():
    print("isSorted([1, 5, 9, 11])", isSorted([1, 5, 9, 11]))
    print("isSorted([11, 6, 7])", isSorted([11, 6, 7]))
    print()
    print("replace('swarthmore', 'x', 'z')", replace("swarthmore", "z", "x"))
    print("replace('hello', 'l', 'y')", replace("hello", "l", "y"))
    print()
    print("reverse('cats')", reverse("cats"))
    print("reverse('hope')", reverse("hope"))
    print()
    print("isPrime(5)", isPrime(5))
    print("isPrime(10)", isPrime(10))

#----------------------------------------------------------------

def isSorted(ls):
    """
    Inputs: A list of numbers
    Returns: True if the list is in ascending order, otherwise False
    Examples:
      isSorted([1, 5, 9, 11]) returns True
      isSorted([11, 6, 7]) returns False
    """
    if len(ls) <= 1:
        return True
    elif ls[0] > ls[1]:
        return False
    else:
        return isSorted(ls[1:])

#----------------------------------------------------------------

def replace(string, old, new):
    """
    Inputs: A string and two characters
    Returns: A new string based on the given string where all
    instances of the character old is replaced by the character new
    Examples:
      replace("swarthmore", "z", "x") returns "swarthmore"
      replace("hello", "l", "y") returns "heyyo"
    """
    if len(string) == 0:
        return string
    elif string[0] == old:
        return new + replace(string[1:], old, new)
    else:
        return string[0] + replace(string[1:], old, new)


#----------------------------------------------------------------

def reverse(string):
    """
    Inputs: A string
    Returns: A new string that is the reverse of the given string
    Examples:
      reverse("cats") returns "stac"
      reverse("hope") returns "epoh"
    """
    if len(string) <= 1:
        return string
    else:
        return reverse(ls[1:]) + string[0]


#----------------------------------------------------------------

def isPrime(n):
    """
    Inputs: An integer
    Returns: True if the number is prime, otherwise False
    Examples:
      isPrime(5) returns True
      isPrime(10) returns False
    This function is complete, you need to write isPrimeHelper.
    """
    return primeHelper(n, 2)

def primeHelper(n, divisor):
    """
    Inputs: Two integers, n and a potential divisor of n
    Returns: False if divisor divides n evenly, otherwise continues
    to test divisors. When all potential divisors have been tested
    and failed up until the square root of n, then return True.
    """
    if divisor > sqrt(n):
        return True
    elif n%divisor == 0:
        print(n, "is divisible by", divisor)
        return False
    else:
        return primeHelper(n,divisor+1)
    return False

main()

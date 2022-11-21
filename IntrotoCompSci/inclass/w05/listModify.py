rfglg"""
This program demonstrates how to pass a list into a function and modify
the list within the function.  Notice that no return statement is needed.
When you change the value at a particular location within a list, you 
have permanently changed it.
"""

def main():
    ls1 = [-10, 90, -1, -45, 12, 22]
    print("Before fixing negatives:", ls1)
    fixNegatives(ls1)
    print("After fixing negatives:", ls1)

def fixNegatives(listOfNums):
    """
    Input: A list of numbers.
    Return: None
    Side effect: Permanently modifes the given list, changing all
    negative values to 0.
    """
    for i in range(len(listOfNums)):
        if listOfNums[i] < 0:
            listOfNums[i] = 0

main()

"""
We will implement several sorting algorithms here.
"""
from random import *

def main():
    myList = [9, 3, 1, 6]

    bubbleSort(myList)
    selectionSort(myList)

def randomList(size, low, high):
    """
    Purpose: Generates a random list of integers for testing.
    Parameters: size for the desired length of the list, the lowest
                possible value, the highest possible value
    Returns: A list of random numbers of the desired size
    """
    ls = []
    for i in range(size):
        ls.append(randrange(low, high+1))
    return ls


def insertionSort(ls):
    """
    Purpose
    """
    numSwaps = 0
    numComps = 0
    for i in range(1, len(ls)):
        j = i
        numComps += 1
        while j > 0 and ls[j] < ls[j-1]:
            numComps += 1
            swap(ls, j, j - 1)
            numSwaps += 1
            j = j - 1
    print("numSwaps", numSwaps, "numComps", numComps)




def isSorted(ls):
    """
    Purpose: To determine if a given list is in sorted order.
    Parameter: A list of items.
    Returns: True if items are in ascending order, otherwise False.
    """
    for i in range(len(ls)-1):
        if ls[i] > ls[i+1]:
            return False

    return True

def bubbleSort(ls):
    """
    Purpose: To sort the given list using the Bubble Sort method.
    Parameter: A list of items.
    Returns: None, the list order is permanently modified.
    """
    n = len(ls)
    for i in range(n-1):
        for j in range(n-1-i):
            if ls[j] > ls[j+1]:
                s = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = s
        print(ls)

def bubbleSort2(ls):
    """
    Purpose: To sort the given list using the Bubble Sort method
    Parameter: A list of items
    Returns: None, the list order is permanently modified
    """
    while True:
        numSwaps = 0
        for i in range(len(ls)-1):
            if ls[i] > ls[i+1]:
                swap(ls, i, i+1)
                numSwaps += 1
        print(ls)

        #    if numSwaps = 0
#    return

def selectionSort(ls):
    """
    Purpose: To sort the given list using the Selection Sort method.
    Parameter: A list of items.
    Returns: None, the list order is permanently modified.
    """
    for i in range(len(ls)):
        indexOfMin = i # location of min item in remaining list
        for j in range(i+1, len(ls)):
            if ls[j] < ls[indexOfMin]:
                indexOfMin = j
        s = ls[indexOfMin]
        ls[indexOfMin] = ls[i]
        ls[i] = s


main()

"""
This program implements and tests two different search algorithms.
It uses randomly generated lists for testing.
"""

from random import *

def main():
    randList = randomList(50, 0, 100)
    print ("List:")
    print(randList)
    randNum = randrange(0,100)
    print("Searching for: %d" % (randNum))
    linear_result = linearSearch(randNum, randList)
    if linear_result == -1:
        print("NOT found")
    else:
        print("Found at position %d" % (linear_result))
    binary_result = binarySearch(randNum, randList)
    if binary_result == -1:
        print("NOT found")
    else:
        print("Found at position %d" % (binary_result))

def randomList(size, low, high):
    """
    Inputs:  size for the desired length of the list, the lowest
             possible value, the highest possible value
    Returns: A list of random numbers of the desired size
    Purpose: Generates a random list for testing
    """
    ls = []
    for i in range(size):
        ls.append(randrange(low,high+1))
    return ls



def linearSearch(item, ls):
    """
    Inputs:  An item we are searching for and a list to search in
    Returns: Index of the found item in the list or -1 if not found
    Purpose: Does a linear search for the item in the list ls
    """
    for i in range(len(ls)):
        if ls[i] == item:
            return i
    return -1

def binarySearch(item, ls):
    """
    Inputs:  An item we are searching for and a SORTED list to search in
    Returns: Index of the found item in the list or -1 if not found
    Purpose: Does a binary search for the item in the SORTED list ls
    """
    low_index = 0
    high_index = 0
    while low_index <= high_index:
        mid_index = int((low_index+high_index)/2)
        if item == ls[mid_index]:
            return mid_index
        elif item < ls[mid_index]:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return -1


if __name__ == '__main__':
    main()
